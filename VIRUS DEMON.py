import os


doll_splash = r"""
=========================================================
          VIRUS DEMON MADE BY Aashish tiwari
                    a ethical hacker
=========================================================
            (q_/p)
            (o.o)
            ==== CONTROL ====
              = ^ =
            .--- ---.
           -.Aashish_________.-
           /   |   |   \
          /    |   |    \
         /     |   |     \
        /      |   |      \

        |_______|_______|
        |   |   |   |   |
        |   |   |   |   |
        (__) (__) (__) (__)
=====================================
 VIRUS IS THE MYSTERIOUS
     MADE BY AaSHISH
=====================================
====================================================================================
ethical hacker - not worth so much but still i am a ethicl hacker Aashish triwari
=====================================================================================
====================================================================================
=================================
"""

print(doll_splash)


username = os.environ.get('USER', os.environ.get('USERNAME', 'User'))
print(f"Hello, user: {username}\n")

print("20 is for black hack virus")
print("21 is for delta virus")

SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))

file_mapping = {
    "20": "20.txt",
    "21": "21.txt",
}

print("Available files to open:")
for selection_key, actual_file in file_mapping.items():
    print(f"- Type {selection_key} to open file: {actual_file}")

user_choice = input("\nEnter the number or name of the file you want to open: ").strip().lower()

chosen_file = None

if user_choice in file_mapping:
    chosen_file = file_mapping[user_choice]
elif user_choice in file_mapping.values():
    chosen_file = user_choice

if chosen_file:
    full_path = os.path.join(SCRIPT_DIR, chosen_file)
    try:
        with open(full_path, 'r', encoding='utf-8') as file_obj:
            content = file_obj.read()
        print(f"\n--- Contents of file {chosen_file} ---")
        print(content)
    except FileNotFoundError:
        print(f"\nError: File {chosen_file} was not found in the script directory.")
        print(f"Expected path: {full_path}")
    except Exception as e:
        print(f"\nError reading file: {e}")
else:
    print(f"\nInvalid selection. '{user_choice}' is not one of the options.")
