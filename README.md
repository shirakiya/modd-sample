# modd-sample
The sample project for modd.  
  
![sample](https://raw.githubusercontent.com/shirakiya/modd-sample/main/docs/sample.gif)  
  
This project is prepared for writing below article.  
https://qiita.com/shirakiya/items/ce7d01c86a5d7b2aafad


# Start
```
# Build the docker image.
$ docker build -t modd-sample:latest .

# Run script with modd.
$ docker run -it --rm -v $(pwd):/opt modd-sample:latest
```
