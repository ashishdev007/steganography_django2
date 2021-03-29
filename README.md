# steganography_django

Steganography is the practice of concealing a message within another message or a physical object. In computing/electronic contexts, a computer file, message, image, or video is concealed within another file, message, image, or video. The advantage of steganography over cryptography alone is that the intended secret message does not attract attention to itself as an object of scrutiny. Plainly visible encrypted messages, no matter how unbreakable they are, arouse interest and may in themselves be incriminating in countries in which encryption is illegal. Whereas cryptography is the practice of protecting the contents of a message alone, steganography is concerned both with concealing the fact that a secret message is being sent and its contents.

This Django application lets you encode your message in a image. You can send this encoded image to anyone and they can retrieve your message from that image using this application.
```
git clone https://github.com/ashishdev007/steganography_django.git
cd steganography_django
docker build -t steganography .
docker run -it -p 8020:8020 steganography
```

Go to http://localhost:8020/ on your browser.

Make sure popups are allowed in your browser.

Note: The retrive hidden messgage function works only for images encoded by this application.
