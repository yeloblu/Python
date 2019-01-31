# WAP to
# take a input string and check if it is a plaindrome

def checkPalindrome(data): 
                          for i in range(0, len(data)/2):
                              if data[i] != str[(len(data)-i)-1]: 
	                                                         print("This is not palindrome"); 
	                      else :
                                    print("This is palindrome"); 

print("Prgram to check palindrome");
data=input("Input string and check if it is a plaindrome:");
checkPalindrome(data) 
print("End of program");
