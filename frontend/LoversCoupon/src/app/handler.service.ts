import { Injectable } from '@angular/core';

interface data{
  "Id": number, 
  "UserId": number, 
  "CouponName": string, 
  "CouponContent": string, 
  "ExpireDate": string, 
  "FromUser": number,
  "CouponStatus": number
}

interface UserAlias{
  "0": string,
  "1": string
}

@Injectable({
  providedIn: 'root'
})
export class HandlerService {

  constructor() { }
  user = 0;

  UA: UserAlias = {
    "0": "寶寶",
    "1": "貝貝"
  }

  username = this.UA[this.user];

  dataList: data[] = [{ 
    "Id": 3, 
    "UserId": 0, 
    "CouponName": "TEST", 
    "CouponContent": "TEST", 
    "ExpireDate": "2020-08-06", 
    "FromUser": 1,
    "CouponStatus": 1 
  },
  { 
    "Id": 4,
    "UserId": 0, 
    "CouponName": "TEST2", 
    "CouponContent": "TEST2", 
    "ExpireDate": "2020-09-06", 
    "FromUser": 1,
    "CouponStatus": 1 
  }
]

}
