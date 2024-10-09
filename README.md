# Strong_Password
Create a strong password

Project description:
This code is designed to test the strength of users' passwords. The tested password must meet several criteria in order to be considered strong according to the required protection.

Criteria for testing:
The password will be considered strong if it meets all of the following criteria:
1. Contain at least one character in lowercase letters - must include at least one of the letters a-z.
2. Contain at least one character in capital letters - must include at least one of the letters A-Z.
3. Contain at least one special character - special characters like @, #, $, %, ^, &, * and more.
4. Contain at least one numeric character - must include at least one of the numbers 0-9.
5. Minimum length of 8 characters - the password must be at least 8 characters long.
6. A character cannot be repeated more than two times - a character cannot be repeated more than two times.
7. No sequences of 3 consecutive characters - the password must not contain a sequence of 3 consecutive characters (such as abc, xyz, 123).

use:
To use the code, you must enter a password and get back a true value (true) if the password meets all the above criteria, or a false value (false) if it does not.

Installation Instructions:
Follow these steps to install and run the strong password validation script.

1. Clone the repository
First, clone the repository to your local machine using the following command:
git clone https://github.com/etic286/sign-up.git

2. Navigate to the project directory
After cloning, navigate to the project directory:
cd repository-name/strongPassword

3. Run the script
Finally, you can run the password validation script by executing:
python Strong_Password.py
The script will ask you to input a password and will validate its strength based on the criteria provided.
