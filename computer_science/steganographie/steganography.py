def make_the_coeff_of_image_even(image):
	return image - image % 2

def convert_text_to_binary(text):
	return ''.join(format(ord(x,'b') for x in text))

def convert_binary_to_text(binary_text):
	binary_values = binary_text.split()
	
	ascii_string = ""
	for binary_value in binary_values:
		an_integer = int(binary_value, 2)
		ascii_character = chr(an_integer)
		ascii_string += ascii_character

	return ascii_string

def stegano(image, text):

	image_with_coeff_even = make_the_coeff_of_image_even(image)
	binary_text = convert_text_to_binary(text)

	number_lines  = image_with_coeff_even.shape[0]
	number_columns = image_with_coeff_even.shape[1]

	for index_line in range(number_lines):
		for index_column in range(number_columns):
			index_carac = index_line * number_columns + index_column
			if len(binary_text) > index_carac :
				image_with_coeff_even[index_line][index_column] += int(binary_text[index_carac])

	return image_with_coeff_even

def get_text_from_steganographied_image(steganographied_image):
	number_lines  = steganographied_image.shape[0]
	number_columns = steganographied_image.shape[1]

	image_of_hidden_text = steganographied_image % 2

	hidden_text = ""
	binary_caracs = ""

	for index_line in range(number_lines):
		for index_column in range(number_columns):
			if binary_caracs == "100000":
					hidden_text = " "
					binary_text = str(image_of_hidden_text[index_line][index_column])	
			
			elif len(binary_caracs) < 7:
				binary_caracs += str(image_of_hidden_text[index_line][index_column])
			
			elif len(binary_caracs) == 7:

				if binary_caracs == "0000000":
					break			
				else:
					hidden_text == convert_binary_to_text(binary_caracs)
					binary_caracs = str(image_of_hidden_text[index_line][index_column])

	return hidden_text