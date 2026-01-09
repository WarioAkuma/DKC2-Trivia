# DKC2 Trivia Database
This repo hosts a Python library for Archipelago that outputs trivia questions in DKC2's format and without format which should help to implement them in other games as long you're exporting this library into your `.apworld`.

This helps me to unlink updating the trivia database with DKC2's apworld updates in the future.

# Submitting questions
You can submit questions via a [Google Form](https://forms.gle/Wh5U2dLMTcYgB64o7) which aims to be a visual aid for understanding the required format or open a Pull Request here with your changes in a `.txt` file.
Questions uploaded by the Google Form will be merged slowly into the repo.

## Creating a txt manually
You may use as an example [this .txt file](https://github.com/TheLX5/DKC2-Trivia/blob/master/data/examples/parser_2_example.txt) to understand how the format works.

The first lines before the first set of `---` corresponds to the file's header, which populates some data about the game such as:
* Parser version (`PARSER`): Usually it's better to leave it at 2.
  * Parser version 1 only allows up to two incorrect answers, version 2 allows three incorrect answers.
  * The third incorrect question is filled as `"None are correct :)"` for Version 1.
* Game name (`GAME`): Self explanatory. It should match a valid topic.
  * Full list of supported topics can be found on the Google Form, I'll be putting docs on that later™️
  * You can only have one game type per `.txt` file
* Author (`AUTHOR`): Your name.
  * Should NOT contain special characters, only A-Z, a-z, 0-9 and underscore characters.
 
The question format should follow this:
* The very first line contains the string `QUESTION:` followed by the difficulty of said question (`EASY`, `MEDIUM`, `HARD`).
* Question goes next and should be up to 6 lines with a maximum of 32 characters each
  * Ideally you should stop at 30 characters per line, as it looks bad in DKC2 when letters reach the borders of the screen
  * The parser will stop processing the question lines until it reads `ANSWERS:` or reaches the 7th line
* Next go the answers for your question. The parser will process exactly four lines after `ANSWERS:`. It'll process three lines if version 1 is used.
  * The first line will **always** be the correct answer
  * Answers should NOT exceed 24 characters
    * However, you can trick the parser into making the answer be two lines long by adding this `°` character as a new line separator. This is mainly a DKC2 quirk.
* Finally, a separator (`---`) **must** be included after entering the last incorrect answer

The filename of the `.txt` file does not matter.

# Interacting with the database as a developer
WIP. I wanted to allow users to contribute to the database while I finish up some details about it.
