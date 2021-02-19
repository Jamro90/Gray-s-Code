#
#	Gray code algebry
#

	# function provide xor gate
def gate_xor(bin1, bin2):

	i = 0
	bit_list = []

	while True:
		try:
			if ((bin1[i] == "0" and bin2[i] == "0") or (bin1[i] == "1" and bin2[i] == "1")):

				bit_list.append("0")

			elif ((bin1[i] == "1" and bin2[i] == "0") or (bin1[i] == "0" and bin2[i] == "1")):

				bit_list.append("1")
		except:
			break
		i = i + 1

	return "".join(map(str, bit_list))

def Gray2bin(bin):

	i = 0
	bit_list = []
	bit_list.append(gate_xor("1", bin[i]))

	while True:
		try:
			bit_list.append(gate_xor(str(bit_list[i]), str(bin[i])))
		except:
			break
		i = i + 1
	bit_list.pop(0)
	i = 0
	while True:
		try:
			if(bit_list[i] == "0"):
				bit_list[i] = "1"
			elif(bit_list[i] == "1"):
				bit_list[i] = "0"
		except:
			break
		i = i + 1
	return "".join(map(str, bit_list))

	# function that add Grey bits
def add_Gray(num1, num2):

	i = len(num1) - 1
	bit_list = []
	num0 = "0"

	while True:
		if(i >= 0):
			if((num1[i] == "0" and num2[i] == "0" and num0 == "0")):
				num0 = "0"
				bit_list.append("0")

			elif(((num1[i] == "0" and num2[i] == "1" and num0 == "0") or (num1[i] == "1" and num2[i] == "0" and num0 == "0") or (num1[i] == "0" and num2[i] == "0" and num0 == "1"))):
				num0 = "0"
				bit_list.append("1")

			elif(((num1[i] == "1" and num2[i] == "1" and num0 == "0") or (num1[i] == "0" and num2[i] == "1" and num0 == "1") or (num1[i] == "1" and num2[i] == "0" and num0 == "1"))):
				num0 = "1"
				bit_list.append("0")

			elif((num1[i] == "1" and num2[i] == "1" and num0 == "1")):
				num0 = "1"
				bit_list.append( "1")
			i = i - 1
		elif(i < 0):
			break

	bit_list.reverse()
	return "".join(map(str, bit_list))

def sub_Gray(num1, num2):

	if(num1 > num2):
		num1 = int(num1, 2)
		num2 = int(num2, 2)
		result = num1 - num2
	return str(bin(result)[2:])

'''	i = len(num1) - 1
	j = 1
	bit_list = []

	while True:
		if(i >= 0):
			if(num1[i] == "1" and num2[i] == "0"):
				bit_list.append("1")

			elif(num1[i] == "1" and num2[i] == "1"):
				bit_list.append("0")

			elif(num1[i] == "0" and num2[i] == "1"):
				while True:
					if(num1[i-j] == "1"):
						num1[i-j].format("0")
						break
					elif(num1[i-j] == "0"):
						j = j + 1
			i = i + 1
		elif(i < 0):
			break
		i = i - 1
	bit_list.reverse()
	return "".join(map(str, bit_list))
'''
def mal_Gray(num1, num2):

	num1 = int(num1, 2)
	num2 = int(num2, 2)
	result = num1 * num2
	return bin(result)[2:]
'''
	i = len(num1) - 1
	j = len(num1) - 1
	z = 0

	bit_list = []

	while(z <= i):
		bit_list.append("0")
		z = z + 1
	row0 = "".join(map(str, bit_list))

	#bit_list.clear()

	while True:
		if(i <= len(num1) - 2):
			row0 = "0" + row0
			bit_list.append( "0")

		if(num2[i] == "0" and i >= 0):
			while True:
				if((j >= 0) and (num1[j] == "0") and (num1[j] == "1")):
					bit_list.append("0")
				elif((j < 0)):
					break
				j = j - 1
		elif(num2[i] == "1" and i >= 0):
			while True:
				if((j >= 0) and (num1[j] == "0")):
					bit_list.append("0")
				elif((j >= 0) and (num1[j] == "1")):
					bit_list.append("1")
				elif(j < 0):
					break
				j = j - 1
		elif(i < 0):
			break
		i = i - 1
		bit_list.reverse()
		print(i)
		print("row0 " + row0)
		print("bit_list "+str(bit_list))

		row1 = "".join(map(str, bit_list))

		result = add_Gray(row1, row0)
		row0 = result
		j = len(num1) - 1
		bit_list.clear()
	return result
'''

def div_Gray(num1, num2):

	num1 = int(num1, 2)
	num2 = int(num2, 2)
	result = num1 / num2
	return bin(result)[2:]

# insert binary data

print("\n##################################################\n")

while True:
	byte1 = input("Wprowadź dane binarne[1]: ")
	byte2 = input("Wprowadź dane binarne[2]: ")

	binData = []

	# funnction checking binary data
	def convert(byte):

		i = 0
		global text
		text = ""

		for bit in byte:

			if byte[i] == "0" or byte[i] == "1":

				binData.append(byte[i])
				text += bit

			else:

				print("Powiedziałem dane binarne!")
				break;

			i += 1

		return text


	text1 = convert(byte1)
	text2 = convert(byte2)
	if len(text1) == len(text2):
		break
	else:
		print("\nDane muszą być w jednym rozszerzeniu!\n")

# show input binary data

if binData == []:
	pass
else:
	print("Dane wprowadzone w binarnym[1]: " + text1)
	print("Dane wprowadzone w binarnym[2]: " + text2)

print("\n##################################################\n")

# decode binary to normal

bin2num1 = int(text1, 2)
bin2num2 = int(text2, 2)

print("Dane wprowadzone w dziesiętnym[1]: " + str(bin2num1))
print("Dane wprowadzone w dziesiętnym[2]: " + str(bin2num2))

print("\n##################################################\n")

# encode binary to Grey's code

data1 = "0" + text1[0:-1]

print("1) Wartość binarna po przesunięciu w prawo[1]: " + str(data1))

print("2) Wynik po bramce XOR: " + str(gate_xor(text1, data1)) + "\n")

data2 = "0" + text2[0:-1]

print("1) Wartość binarna po przesunięciu w prawo[2]: " + data2)

print("2) Wynik po bramce XOR: " + str(gate_xor(text2, data2)))

print("\n##################################################\n")

xor1 = str(gate_xor(text1, data1))
xor2 = str(gate_xor(text2, data2))

choose = input("Wybierz operację bitową [+, -, *, /]: ")

# bitwise operation

if choose == "+":

	print("\nWynik dodawania:  " + str(add_Gray(xor1, xor2)))
	print("Wynik otrzymany dziesiętnie: " + str(int(str(Gray2bin(str(add_Gray(xor1, xor2)))), 2)))

	print("\nWynik prawidłowy: " + str(add_Gray(text1, text2)))
	print("Wynik dziesiętny: " + str(int(str(add_Gray(text1, text2)), 2)))

elif choose == "-":

	print("\nWynik odejmowania: " + str(gate_xor("0" + sub_Gray(xor1, xor2), sub_Gray(xor1, xor2))))
	print("Wynik otrzymany dziesiętnie: " + str(int(str(sub_Gray(xor1, xor2)), 2)) )

	print("\nWynik prawidłowy: " + str(sub_Gray(text1, text2)))
	print("Wynik dziesiętny: " + str(int(sub_Gray(text1, text2), 2)))

elif choose == "*":

	print("\nWynik mnożenia: " + str(gate_xor("0" + mal_Gray(xor1, xor2), mal_Gray(xor1, xor2))))
	print("Wynik otrzymany dziesiętnie: " + str(int(str(mal_Gray(xor1, xor2)), 2)) )

	print("\nWynik prawidłowy: " + str(mal_Gray(text1, text2)))
	print("Wynik dziesiętny: " + str(int(mal_Gray(text1, text2), 2)))

elif choose == "/":

	print("\nWynik dzielenia: " + str(gate_xor("0" + div_Gray(xor1, xor2), div_Gray(xor1, xor2))))
	print("Wynik otrzymany dziesiętnie: " + str(int(str(div_Gray(xor1, xor2)), 2)) )

	print("\nWynik prawidłowy: " + str(div_Gray(text1, text2)))
	print("Wynik dziesiętny: " + str(int(div_Gray(text1, text2), 2)))




