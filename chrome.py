import webbrowser
new = 2
url='http://google.com'
chrome_path = 'C:/Program Files (x86)/Google/Chrome/Application/chrome.exe %s'
webbrowser.get('windows-default').open(url, new=new)
