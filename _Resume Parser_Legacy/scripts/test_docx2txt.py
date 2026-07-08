import docx2txt

file = r"D:\Recruitment Automation Version 2\Resume Parser\Input\Naukri_BMRaghavendra[8y_0m].docx"

text = docx2txt.process(file)

print("=" * 60)
print(text[:3000])
print("=" * 60)