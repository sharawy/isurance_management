# Insurance mangement app
Simple app to add insurance policies to customers

# Requirements
   - python version 3.*
   
# Setup 
```bash
pip install -r requirments.txt
python manage.py makemigrations
python manage.py migrate
```

# Running local server
```bash
python manage.py runserver

```
#### Examples:
- **Create customer**
    - Path: api/v1/customers/
    - method: POST
    - body: 
        ```json
        {
        "first_name": "Ben",
        "last_name": "Stokes",
        "dob": "25-06-1991"
        }
        ```
- **Create policy**
    - Path: api/v1/policies/
    - method: POST
    - body: 
        ```json
        {
            "type": "personal-accident",
            "premium": "3333.00",
            "cover": "333333.00"
        }
        ```
- **Add policy to customer**
    - Path: /api/v1/customers/{customer_id}/policies/
    - method: PUT
    - body: 
        ```json
        {
            "policies": [policy_id, policy_id]
        }
        ```
- **Remove policy to customer**
    - Path: /api/v1/customers/{customer_id}/policies/
    - method: DELETE
    - body: 
        ```json
        {
            "policies": [policy_id, policy_id]
        }
        ```
**Note: You can import the postman collection and test the api**

# Test

```bash
python manage.py test
```
