//: Playground - noun: a place where people can play

import UIKit

var result: [Int] = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0] //각 숫자의 갯수를 저장할 배열을 만듦

for i in 1...1000 { //1~1000까지 반복
    
    let string = Array(String(i).characters)
    
    for c in string {
        
        if let index = Int(String(c)) { //인덱스의 값과 숫자의 값을 비교하여 맞으면 인덱스에 1증가
            
            result[index] = result[index] + 1
        }
    }
}

for i in 0...9 { //배열 출력
    print("\(i) : \(result[i])")
}

