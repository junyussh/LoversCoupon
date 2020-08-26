# LoversCoupon

練習 HTML + JavaScript + Flask 的小專案，想不到主題，就幫情侶們做一個"交換券"管理平台，就是那種憑券兌換XXX之類的東西。

## 後端架構
- Programming language: Python
- Web framework: Flask
- Database: SQLite

## Run backend

```json
pip install pipenv
pipenv shell
cd backend/
pipenv install

python app.py
```

## TODO

### Basic
- [ ] Complete backend database
- [ ] Complete add.html feature
- [ ] Add expire coupon check
- [ ] Add delete coupon feature

### Security
- [ ] Session check
- [ ] Account authorization
- [ ] Handle server error conditions
