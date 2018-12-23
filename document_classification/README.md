# API

### Endpoints
- Health check `GET /api`
```bash
curl --header "Content-Type: application/json" \
     --request GET \
     http://localhost:5000/
```

- Training `POST /train`
```bash
curl --header "Content-Type: application/json" \
     --request POST \
     --data '{"config_filepath": "/Users/goku/Documents/productionML/document_classification/configs/train.json"}' \
     http://localhost:5000/train
```

- List of experiments `GET /experiments`
```bash
curl --header "Content-Type: application/json" \
     --request GET \
     http://localhost:5000/experiments
```

- Experiment info `GET /experiment_info/<experiment_id>`
```bash
curl --header "Content-Type: application/json" \
     --request GET \
     http://localhost:5000/info/latest
```

- Delete an experiment
```bash
curl --header "Content-Type: application/json" \
     --request GET \
     http://localhost:5000/delete/1545593561_8371ca74-06e9-11e9-b8ca-8e0065915101
```