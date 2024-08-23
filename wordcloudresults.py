from wordcloud import WordCloud
import matplotlib.pyplot as plt

# Provided phrases related to phishing and not phishing
phishing_phrases = [
    "The url looks extremely sus", "Looks fishy", "Bad casing, bad grammar, bad formatting, etc",
    "Incorrect grammar, no logos", "Lack of capitalization on the first letter", "It looks like a normal typed email",
    "It has a lack of proper punctuation such as capital letters etc.", "Incorrect punctuation", 
    "It is common for phones to be used in phishing"
]

not_phishing_phrases = [
    "Briefly, what made you think it was a legitimate message?", 
    "It contained specifics about what the person ordered as well as a tracking link once the order is dispatched.",
    "Usually companies have a business card attached to the bottom of the email as well as an order number",
    "They regarded Jone by name, they provided specific information regarding his purchase and they did provide information such as an email",
    "The format of the email was nothing like a legitimate order confirmation email",
    "Utilized my name and product that had been brought. If that specific model of phone had not been brought then I would think it is fake, however I don't have this info.",
    "Yes it provides a tracking link", "Seems reputable", "I would know if I purchased it or not"
]

# Join all the phishing and not phishing phrases into separate strings
phishing_text = ' '.join(phishing_phrases)
not_phishing_text = ' '.join(not_phishing_phrases)

# Generate word clouds for phishing and not phishing phrases
phishing_wordcloud = WordCloud(width=800, height=400, background_color='white', colormap='Reds').generate(phishing_text)
not_phishing_wordcloud = WordCloud(width=800, height=400, background_color='white', colormap='Greens').generate(not_phishing_text)

# Plot the word clouds
plt.figure(figsize=(12, 6))

plt.subplot(1, 2, 1)
plt.imshow(phishing_wordcloud, interpolation='bilinear')
plt.title('Phishing Phrases')
plt.axis('off')

plt.subplot(1, 2, 2)
plt.imshow(not_phishing_wordcloud, interpolation='bilinear')
plt.title('Not Phishing Phrases')
plt.axis('off')

plt.show()


from wordcloud import WordCloud
import matplotlib.pyplot as plt

# Provided key phrases related to usernames and passwords
username_password_keywords = [
    "username and password", "It should know my password", "not send password", "already have these details",
    "bad grammar", "asked for email and password", "no specific information", "company never asks this",
    "asks for personal info", "IT should have access already", "companies shouldn't ask for password",
    "vague email and generic greeting", "password", "password and username shouldn't be shared"
]

# Splitting keywords into good and bad practices


bad_practices = [phrase for phrase in username_password_keywords]

# Join all the keywords into separate strings

bad_text = ' '.join(bad_practices)

# Generate word clouds for good and bad practices
bad_wordcloud = WordCloud(width=800, height=400, background_color='white', colormap='Reds').generate(bad_text)

# Plot the word clouds
plt.figure(figsize=(12, 6))

plt.subplot(1, 2, 1)
plt.imshow(bad_wordcloud, interpolation='bilinear')
plt.title('Good Practices')
plt.axis('off')



plt.show()

from wordcloud import WordCloud
import matplotlib.pyplot as plt

# Provided key phrases related to banking security
bank_security_keywords = [
    "number present", "email link only sent out by bank", "url suspicious", "personal info private",
    "would call the bank", "bad casing", "similar student finance scam", "banks dont contact you",
    "specific account info", "change password", "banks would ask you to do it on phone",
    "dont click link", "dont click link call", "phone number in email isnt halifax real phone number",
    "link", "account number", "provides account details", "should hash but could be real",
    "anything banking should call me"
]

# Classify phrases into genuine or not
genuine_phrases = [
    "number present", "email link only sent out by bank", "personal info private",
    "would call the bank", "banks dont contact you", "specific account info",
    "banks would ask you to do it on phone", "phone number in email isnt halifax real phone number",
    "should hash but could be real", "anything banking should call me"
]

# Separate phrases into genuine and not genuine
genuine_phrases = [phrase for phrase in bank_security_keywords if phrase in genuine_phrases]
not_genuine_phrases = [phrase for phrase in bank_security_keywords if phrase not in genuine_phrases]

# Join all the genuine and not genuine phrases into separate strings
genuine_text = ' '.join(genuine_phrases)
not_genuine_text = ' '.join(not_genuine_phrases)

# Generate word clouds for genuine and not genuine phrases
genuine_wordcloud = WordCloud(width=800, height=400, background_color='white', colormap='Greens').generate(genuine_text)
not_genuine_wordcloud = WordCloud(width=800, height=400, background_color='white', colormap='Reds').generate(not_genuine_text)

# Plot the word clouds
plt.figure(figsize=(12, 6))

plt.subplot(1, 2, 1)
plt.imshow(not_genuine_wordcloud, interpolation='bilinear')
plt.title('Genuine Phrases')
plt.axis('off')

plt.subplot(1, 2, 2)
plt.imshow(genuine_wordcloud, interpolation='bilinear')
plt.title('Not Genuine Phrases')
plt.axis('off')

plt.show()


from wordcloud import WordCloud
import matplotlib.pyplot as plt

# Provided reasons why the email might be genuine
reasons_genuine = [
    "It contained specifics such as order number and estimated delivery date as well as providing contact examples for customer service.",
    "There are no links that could possibly be dangerous, and the order number is stated.",
    "Mostly cause it didnt mention contacting them through any emails or anything. Just a notification.",
    "Because it tells you to go to the trusted app",
    "Not asking for anything",
    "Quite a passive email - doesn't prompt for any personal or sensitive info to be entered. Was sent to John right after he made the purchase. Good structure, format, grammar, etc.",
    "It didn’t actually ask for any information or ask me to click or go anywhere, it was purely informing me that my package was due to arrive and did not ask me to go any further.",
    "Specific information provided, addressed by name, no response required preventing any reason for information to go out.",
    "No links provided, no asking for any passwords, and they even use their own (very likely well-moderated) app to track packages rather than a link or website.",
    "There are no links in the email, and the order ID is included in the email. If the order ID is consistent with the order John made, as well as there are no prompts to click any links in the email, it is unlikely to be a phishing scam. However, there is a likelihood the order ID was still intercepted.",
    "The email doesn't contain any links and directs you to go to the customer service without a link. This email is also responsive to John placing an order so is expected.",
    "It gives no added information or requires the need to go to another location, this also looks like a normal confirmation email.",
    "The layout of the email and the language used.",
    "It is not asking for any information from the recipient, and John can compare the order ID in the email to that on Amazon's website to make sure it's genuine.",
    "No dodgy URLs.",
    "They give the order number, and the email isn't asking the user for anything.",
    "It provides order details.",
    "It contains delivery date.",
    "it provides delivery date"
]

# Provided reasons why the email might not be genuine
reasons_not_genuine = [
    "Doesn't have Delivery address in email",
    
]

# Generate word cloud for reasons why the email might be genuine
genuine_reason_wordcloud = WordCloud(width=800, height=400, background_color='white', colormap='Greens').generate(' '.join(reasons_genuine))

# Generate word cloud for reasons why the email might not be genuine
not_genuine_reason_wordcloud = WordCloud(width=800, height=400, background_color='white', colormap='Reds').generate(' '.join(reasons_not_genuine))

# Plot the word clouds
plt.figure(figsize=(12, 6))

plt.subplot(1, 2, 1)
plt.imshow(not_genuine_reason_wordcloud, interpolation='bilinear')
plt.title('Genuine Reasons')
plt.axis('off')

plt.subplot(1, 2, 2)
plt.imshow(genuine_reason_wordcloud, interpolation='bilinear')
plt.title('Not Genuine Reasons')
plt.axis('off')

plt.show()

