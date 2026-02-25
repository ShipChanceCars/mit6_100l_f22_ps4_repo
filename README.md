# **mit6_100l_f22_ps4_repo**

This is the repository for solving Problem Set 4 in MIT 6_100l_f22.

## *The setup is complete*

All the files for ps4 are now in GitHub including the solved "ps4a.py".

## *Parts A&B are complete*

In Part A: Recursive Operations on Trees I've used the Node object to represent trees.
Then the function find_tree_height has been implemented using recursion. Lastly, the
function is_heap has been written to check whether a tree is a max or min heap.
In Part B: Encryption with One Time Pads I've completed three classes that allow
user to use one time pad encryption. Message is the parent class which contains methods
that both plaintext and ciphertext can employ. PlaintextMessage class contains methods
that are applicable to the original message, such as generating a one time pad or
encrypting a message. Similarly, EncryptedMessage class has got methods that are
specific to the ciphertext, such as decrypting a message using one time pad.

## *Part C*

Part C focuses on using our own classes created in Part B. I've finished the function
decrypt_message_try_pads that receives a ciphertext and a list of the possible pads used
to encrypt it and returns returns the original message and the correct pad. It does so by
decrypting the ciphertext with each pad and counting the number of real words in it. This
is achieved by comparing each word in the decrypted output with the large list of English
words in the separate file. The correct pad is assumed to be the one which produces the 
biggest number of valid words. If a tie occurs, the last pad that returns the maximum
number of English words is chosen. The function decode_story is now working. It invokes
get_story_string to get the ciphertext from the text file, then get_story_pads grabs the
list of one time pads from the text file. The penultimate step is the call to 
decrypt_message_try_pads function implemented before. It returns PlaintextMessage object.
The last step is extracting the string repersentation from the object and returning it.