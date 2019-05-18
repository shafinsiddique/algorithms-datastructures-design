"""This section consists of leetcode easy questions from the Strings Section."""
def toLowerCase(s: str) -> str:
    """THis function returns a string in all lowercase."""

    return s.lower()

def uniqueMorseCodes(l: list) -> int:
    morse = [".-","-...","-.-.","-..",".","..-.",
             "--.","....","..",".---","-.-",".-..",
             "--","-.","---",".--.","--.-",".-.","...",
             "-","..-","...-",".--","-..-","-.--","--.."]

    converted = []
    for strs in l:
        translation = ""

        for characters in strs:
            # print(ord(characters)-96-1)
            translation+= morse[ord(characters)-96-1]

        converted.append(translation)

    final_list = []

    for words in converted:
        if words not in final_list:
            final_list.append(words)

    return len(final_list)


def unique_email_address(e: list) -> int:
    mailing_list = []

    for emails in e:
        # can be optimized here if we write an if statement.
        localname = emails[:emails.index("@")-1]

        temp_email = ""

        for chars in localname[:localname.index("+")-1]:
            if chars != ".":
                temp_email += chars

        temp_email += emails[emails.index("@"):]

        if temp_email not in mailing_list:
            mailing_list.append(temp_email)

    return len(mailing_list)


print(unique_email_address(["test.email+alex@leetcode.com","test.e.mail+bob.cathy@leetcode.com","testemail+david@lee.tcode.com"]))