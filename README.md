simplest flask dockerised API with github actions
```
docker build -t isEven:latest .
docker run -it -p 5000:5000 --rm isEven:latest

curl -X POST  -H "Content-Type: application/json" --data '[1]' http://0.0.0.0:5000/isEven
'''
