answer = input("Please give a filename: ")
if answer.lower().strip().endswith(".gif"):
    print("image/gif")
elif answer.lower().strip().endswith(".jpg"):
    print("image/jpeg")
elif answer.lower().strip().endswith(".jpeg"):
    print("image/jpeg")
elif answer.lower().strip().endswith(".png"):
    print("image/png")
elif answer.lower().strip().endswith(".pdf"):
    print("application/pdf")
elif answer.lower().strip().endswith(".txt"):
    print("text/plain")
elif answer.lower().strip().endswith(".zip"):
    print("application/zip")
else:
    print("application/octet-stream")