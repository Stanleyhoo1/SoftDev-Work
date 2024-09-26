Prediction: When accessing "http://localhost:5000/static/foo" it will just print the text.
Actual: It downloads the file foo

you can access foo.html by calling the h() function within the hello_world function

accessing foo.html using the path returns the html page, while calling the path in Python returns whatever is after the return statement