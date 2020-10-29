from tkinter import messagebox, simpledialog, Tk

main = Tk()
main.withdraw()


def get_task():
    task = simpledialog.askstring('Task', 'Do you want to encrypt or decrypt')
    return task


def get_message():
    message = simpledialog.askstring('Message', 'Enter secret message :')
    return message


def is_even(number):
    return number % 2 == 0


def get_even(message):
    even_letter = []
    for i in range(len(message)):
        if is_even(i):
            even_letter.append(message[i])
    return even_letter


def get_odd(message):
    odd_letter = []
    for i in range(len(message)):
        if not is_even(i):
            odd_letter.append(message[i])
    return odd_letter


def swap_letters(message):
    letter_list = []
    if not is_even(len(message)):
        message = message + '~'
    even_letters = get_even(message)
    odd_letters = get_odd(message)
    for counter in range(0, len(message)//2):
        letter_list.append(odd_letters[counter])
        letter_list.append(even_letters[counter])
    new_message = ''.join(letter_list)
    return new_message


def encrypt(msg):
    encrypted = swap_letters(msg)
    encrypt_msg = "".join(reversed(encrypted))
    return encrypt_msg


def decrypt(msg):
    message = "".join(reversed(msg))
    decrypted_msg = swap_letters(message)
    decrypted_msg = decrypted_msg.replace('~', "")
    return decrypted_msg


while True:
    task = get_task().lower().strip()
    if task == 'encrypt':
        message = get_message()
        encrypted = encrypt(message)
        messagebox.showinfo('Cipher text ', encrypted)
    elif task == 'decrypt':
        message = get_message()
        decrypted = decrypt(message)
        messagebox.showinfo('Plain text ', decrypted)
    else:
        break
        main.destroy()

main.mainloop()
