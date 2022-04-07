#!/bin/bash

aws dynamodb put-item --table-name "VACCINATION_RESERVATION" \
  --item \
  '{"pk": {"S": "slot#1"},"reservation_date":{"S": "2021-11-14 13:45:00"},"location":{"S": "Tokyo"}}'

aws dynamodb put-item --table-name "VACCINATION_RESERVATION" \
  --item \
  '{"pk": {"S": "slot#2"},"reservation_date":{"S": "2021-11-14 14:00:00"},"location":{"S": "Tokyo"}}'

aws dynamodb put-item --table-name "VACCINATION_RESERVATION" \
  --item \
  '{"pk": {"S": "slot#3"},"reservation_date":{"S": "2021-11-14 14:15:00"},"location":{"S": "Tokyo"}}'

aws dynamodb put-item --table-name "VACCINATION_RESERVATION" \
  --item \
  '{"pk":{"S": "recipient#1"},"email":{"S": "fatsushi@example.com"},"first_name":{"S": "Atsushi"},"last_name":{"S": "Fukui"},"age":{"N":"20"}, "slots": {"L":[]}}'
