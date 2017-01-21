#include <stdio.h>
#include <cs50.h>
#include <stdlib.h>
#include <string.h>
#include <ctype.h>

int main(int argc, string argv[])
{
    int key, cipherletter;
    string plaintext;

// check command input: remind usage and quit if the input is incorrect
    // the command takes one argument only
    if (argc != 2)
    {
        printf("Usage: ./caesar <key>\n");
        printf("You should provide one and only one argument.\n");
        return 1;
    }

    // the argument must be a non-negative integer
    else if (atoi(argv[1]) < 0)
    {
        printf("Usage: ./caesar <key>\n");
        printf("Cipher key must be a non-negative integer.\n");
        return 1;
    }

// encrypt the plaintext
    else
    {
        key = atoi(argv[1]);

        // ask the user for the plaintext to encrypt
        plaintext = GetString();

        // encrypt each character of the plaintext
        for (int i = 0, n = strlen(plaintext); i < n; i++)
        {

            // no action on digits, spaces and punctuation
            if (isdigit(plaintext[i]) || isspace(plaintext[i])
                || ispunct(plaintext[i]))
            {
                printf("%c", plaintext[i]);
            }

            // encrypt letters
            else
            {
                // encrypt uppercase letters
                if (isupper(plaintext[i]))
                {
                    // if wrapping from "Z" to "A" is required
                    // a modulus calculation is carried out (% 26, the number of
                    // letters in the English alphabet), but the ASCII numeric
                    // value of the first letter of the alphabet is substracted
                    // before the modulus calculation ("A" is treated as 0,
                    // "Z" is treated as 25) and added back to the result,
                    // so that the letter shift occurs on the actual
                    // ASCII uppercase alphabet sequence ("A" is 65, "Z" is 90)
                    if ((plaintext[i] + key) <= 64
                        || (plaintext[i] + key) >= 91)
                    {
                        cipherletter = (((plaintext[i] - 65) + key) % 26) + 65;
                    }
                    // if no wrapping from "Z" to "A" is required
                    // the key is added to the ASCII numeric value of the letter
                    else
                    {
                        cipherletter = (plaintext[i] + key);
                    }
                    // print each encrypted letter to display ciphertext
                    printf("%c", cipherletter);
                }

                // encrypt lowercase letters
                else if (islower(plaintext[i]))
                {
                    // if wrapping from "z" to "a" is required
                    // a modulus calculation is carried out (% 26, the number of
                    // letters in the English alphabet), but the ASCII numeric
                    // value of the first letter of the alphabet is substracted
                    // before the modulus calculation ("A" is treated as 0,
                    // "Z" is treated as 25) and added back to the result,
                    // so that the letter shift occurs on the actual
                    // ASCII uppercase alphabet sequence ("a" is 97, "z" is 122)
                    if ((plaintext[i] + key) <= 96
                        || (plaintext[i] + key) >= 123)
                    {
                        cipherletter = (((plaintext[i] - 97) + key) % 26) + 97;
                    }
                    // if no wrapping from "z" to "a" is required
                    // the key is added to the ASCII numeric value of the letter
                    else
                    {
                        cipherletter = (plaintext[i] + key);
                    }
                    // print each encrypted letter to display ciphertext
                    printf("%c", cipherletter);
                }
                else
                    printf("");
            }
        }
        printf("\n");
    }
    return 0;
}
