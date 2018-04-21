#encoding: utf-8
import random
import struct, hashlib
import time, re

#4字节
def Endian(b): 
  return [struct.unpack('<I', ''.join(b[i:i+4]))[0] for i in range(0, len(b), 4)]

#循环左/右移
def LeftRot(n, b): return ((n << b) | ((n & 0xffffffff) >> (32 - b))) & 0xffffffff
def RightRot(n, b): return ((n >> b) | ((n & 0xffffffff) << (32 - b))) & 0xffffffff

#MD4中的函数
def F(x, y, z): return x & y | ~x & z
def G(x, y, z): return x & y | x & z | y & z
def H(x, y, z): return x ^ y ^ z

def FF(a, b, c, d, k, s, X): return LeftRot(a + F(b, c, d) + X[k], s)
def GG(a, b, c, d, k, s, X): return LeftRot(a + G(b, c, d) + X[k] + 0x5a827999, s)
def HH(a, b, c, d, k, s, X): return LeftRot(a + H(b, c, d) + X[k] + 0x6ed9eba1, s)

#计算MD4
def MD4(m): 
  md4 = hashlib.new('md4')
  md4.update(m)
  return md4.hexdigest()

#第一轮修改
def FirstRound(abcd, j, i, s, x, constraints):
  v = LeftRot(abcd[j%4] + F(abcd[(j+1)%4], abcd[(j+2)%4], abcd[(j+3)%4]) + x[i], s)
  for constraint in constraints:
    if   constraint[0] == '=': v ^= (v ^ abcd[(j+1)%4]) & (2 ** constraint[1]) #等于下一个链变量
    elif constraint[0] == '0': v &= ~(2 ** constraint[1]) # =0的位
    elif constraint[0] == '1': v |= 2 ** constraint[1] # =1的位
    
  #反推，更新m
  x[i] = (RightRot(v, s) - abcd[j%4] - F(abcd[(j+1)%4], abcd[(j+2)%4], abcd[(j+3)%4])) % 2**32
  abcd[j%4] = v #更新链变量

def FindCollision(m):
  x = Endian(m) # 小端序
  initial_abcd = [0x67452301, 0xefcdab89, 0x98badcfe, 0x10325476]
  abcd = initial_abcd[:]
  
  #第一轮的所有条件
  # constraints = [
  #   [['=', 6]],
  #   [['0', 6],['=', 7],['=', 10]],
  #   [['1', 6],['1', 7],['0', 10],['=', 25]],
  #   [['1', 6],['0', 7],['0', 10],['0', 25]],
  #   [['1', 7],['1', 10],['0', 25],['=', 13]],
  #   [['0', 13],['=', 18],['=', 19],['=', 20],['=', 21],['1', 25]],
  #   [['=', 12],['0', 13],['=', 14],['0', 18],['0', 19],['1', 20],['0', 21]],
  #   [['1', 12],['1', 13],['0', 14],['=', 16],['0', 18],['0', 19],['0', 20],['0', 21]],
  #   [['1', 12],['1', 13],['1', 14],['0', 16],['0', 18],['0', 19],['0', 20],['=', 22],['1', 21],['=', 25]],
  #   [['1', 12],['1', 13],['1', 14],['0', 16],['0', 19],['1', 20],['1', 21],['0', 22],['1', 25],['=', 29]],
  #   [['1', 16],['0', 19],['0', 20],['0', 21],['0', 22],['0', 25],['1', 29],['=', 31]],
  #   [['0', 19],['1', 20],['1', 21],['=', 22],['1', 25],['0', 29],['0', 31]],
  #   [['0', 22],['0', 25],['=', 26],['=', 28],['1', 29],['0', 31]],
  #   [['0', 22],['0', 25],['1', 26],['1', 28],['0', 29],['1', 31]],
  #   [['=', 18],['1', 22],['1', 25],['0', 26],['0', 28],['0', 29]],
  #   [['0', 18],['=', 25], ['1', 26],['1', 28],['0', 29],['=', 31]]
  # ]

 
  constraints = [
    [
      ['=', 6]
    ],
    [
      ['0', 6],
      ['=', 7],
      ['=', 10]
    ],
    [
      ['1', 6],
      ['1', 7],
      ['0', 10],
      ['=', 25]
    ],
    [
      ['1', 6],
      ['0', 7],
      ['0', 10],
      ['0', 25]
    ],
    [
      ['1', 7],
      ['1', 10],
      ['0', 25],
      ['=', 13]
    ],
    [
      ['0', 13],
      ['=', 18],
      ['=', 19],
      ['=', 20],
      ['=', 21],
      ['1', 25]
    ],
    [
      ['=', 12],
      ['0', 13],
      ['=', 14],
      ['0', 18],
      ['0', 19],
      ['1', 20],
      ['0', 21]
    ],
    [
      ['1', 12],
      ['1', 13],
      ['0', 14],
      ['=', 16],
      ['0', 18],
      ['0', 19],
      ['0', 20],
      ['0', 21]
    ],
    [
      ['1', 12],
      ['1', 13],
      ['1', 14],
      ['0', 16],
      ['0', 18],
      ['0', 19],
      ['0', 20],
      ['=', 22],
      ['1', 21],
      ['=', 25]
    ],
    [
      ['1', 12],
      ['1', 13],
      ['1', 14],
      ['0', 16],
      ['0', 19],
      ['1', 20],
      ['1', 21],
      ['0', 22],
      ['1', 25],
      ['=', 29]
    ],
    [
      ['1', 16],
      ['0', 19],
      ['0', 20],
      ['0', 21],
      ['0', 22],
      ['0', 25],
      ['1', 29],
      ['=', 31]
    ],
    [
      ['0', 19],
      ['1', 20],
      ['1', 21],
      ['=', 22],
      ['1', 25],
      ['0', 29],
      ['0', 31]
    ],
    [
      ['0', 22],
      ['0', 25],
      ['=', 26],
      ['=', 28],
      ['1', 29],
      ['0', 31]
    ],
    [
      ['0', 22],
      ['0', 25],
      ['1', 26],
      ['1', 28],
      ['0', 29],
      ['1', 31]
    ],
    [
      ['=', 18],
      ['1', 22],
      ['1', 25],
      ['0', 26],
      ['0', 28],
      ['0', 29]
    ],
    [
      ['0', 18],
      ['=', 25], # could also be ['1', 25]
      ['1', 26],
      ['1', 28],
      ['0', 29],
      ['=', 31]  # extra constraint from Naito, et al.
    ],
  ]

  shift = [3, 7, 11, 19] * 4
  change = [0, 3, 2, 1] * 4

  #使满足第一轮的所有条件
  for i in range(16):
    FirstRound(abcd, change[i], i, shift[i], x, constraints[i])
  
 
  m = ''.join([struct.pack('<I', i) for i in x])
  m_ = CreateCollision(m) #碰撞微分

  if MD4(m) == MD4(m_):
    return m, m_
   
  return None, None

#对于修正后的M，有一定概率可以通过碰撞微分找到M'
def CreateCollision(m):
  x = list(Endian(m))
  x[1] = (x[1] + (2 ** 31)) % 2**32
  x[2] = (x[2] + ((2 ** 31) - (2 ** 28))) % 2**32
  x[12] = (x[12] - (2 ** 16)) % 2**32
  return ''.join([struct.pack('<I', i) for i in x])

def Collision():
  num = 1
  while 1:
    #随机的M
    m = [chr(i) for i in [random.randint(0, 2 ** 8 - 1) for i in range(64)]]
    ma, mb = FindCollision(m)
    if ma:
      #winsound.Beep(600, 1000)
      break
    num += 1
    if(num%100000==0):
      print(num,'\n')
  
  h1 = MD4(ma)
  h2 = MD4(mb)
  # return ma, mb, h1, h2
  return ma.encode('hex'), mb.encode('hex'), h1, h2

# main()
time.clock()
print '[+]Finding Collision...'
m1, m2, h1, h2 = Collision()
M1 = re.findall('.{4}', m1)
M2 = re.findall('.{4}', m2)

mm1 = ''
mm2 = ''
for i in range(len(M1)):
  if M1[i] != M2[i]:
    mm1 += '[' + M1[i] + ']'
    mm2 += '[' + M2[i] + ']'
  else:
    mm1 += M1[i]
    mm2 += M1[i]
    
print "  [-]The M1 is:", m1
print "  [-]The M2 is:", m2
print "  [-]M1 and M2 diff:\n    [*]" + mm1 + "\n    [*]" + mm2
print "  [-]The MD4(M1) is:", h1
print "  [-]The MD4(M2) is:", h2
print "[!]M1 == M2 ?", m1 == m2
print "[!]MD4(M1) == MD4(M2) ?", h1 == h2
print "[!]All d1!"
print "[!]Timer:", round(time.clock(), 2), "s"

# The diff in:
# m1[1] m2[1]
# m1[2] m2[2] 
# m1[12] m2[12]