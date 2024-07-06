# print("백문이 불여일견\n백견이 불여일타")
#
# print('저는 "나도코딩"입니다.')
#
# print("저는 \"나도코딩\"입니다.")
#
# print("C:\\Users\\LG\\AppData\\Local\\Microsoft\\WindowsApps\\python3.12.exe")
#
# print("aaaaaaaaaaaaaaaaaaaaa \rhellolleh")
#
# print("redd\bapple")
#
# print("red\tapple") #tab

url = "https://naver.com"
my_str = url.replace("https://", "")
my_str = my_str[:my_str.index(".")] # my_str[0:5]
password = my_str[:3] + str(len(my_str)) + str(my_str.count("e")) + "!"
print('{0} 의 비밀번호는 {1}입니다.'.format(url, password))