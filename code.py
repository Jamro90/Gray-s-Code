#
#	Gray code algebry
#

	# function provide xor gate
def gate_xor(bin1, bin2):

	i = 0
	bit_list = []

	while True:
		try:
			if ((bin1[i] == "0" and bin2[i] == "0")):

				bit_list.append("1")

			elif((bin1[i] == "1" and bin2[i] == "1")):

				bin_list.append("1")

			elif ((bin1[i] == "1" and bin2[i] == "0") or (bin1[i] == "0" and bin2[i] == "1")):

				bit_list.append("0")
		except:
			break
		i = i + 1

	return "".join(map(str, bit_list))

	# function that add Grey bits
def add_Grey(num1, num2):

#	if num1[i] == "0" and num2[i] == "0":
#		data.append("0")
#	elif ((num1[i] == "1" and num2[i] == "0") or num1[i] == "0" and num2[i] == "1")):
#		data.append("1
	for a, b in zip(num1[::-1], num2[::-1]):
		global data
		data = a & b
	return data

def sub_Grey(num1, num2):

	for a, b in zip(num1[::-1], num2[::-1]):
		global data
		data = a | b
	return data

def mal_Grey(num1, num2):
	pass
def div_Grey(num1, num2):
	pass

# insert binary data

print("\n##################################################\n")

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

print("Wartość binarna po przesunięciu w prawo[1]: " + str(data1))

print("Wynik po bramce XOR: " + str(gate_xor(text1, data1)))

print("Zapis w kodzie Gray'a: " + "\n")

data2 = "0" + text2[0:-1]

print("Wartość binarna po przesunięciu w prawo[2]: " + data2)

print("Wynik po bramce XOR: " + str(gate_xor(text2, data2)))

print("Zapis w kodzie Gray'a: " )

print("\n##################################################\n")

choose = input("Wybierz operację bitową [&, |, <<, >>]: ")

# bitwise operation

if choose == "&":
	add_Grey(data1, data2)
elif choose == "|":
	sub_Grey(data1, data2)
elif choose == "<<":
	mal_Grey(data1, data2)
elif choose == ">>":
	div_Grey(data1, data2)




