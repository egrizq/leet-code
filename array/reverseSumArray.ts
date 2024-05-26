function reverseSumArray(arr:number[]): number[] {
    let ans: number[] = []
    let sum = 0
    for (let n = arr.length-1; n >= 0; n--) {
        sum += arr[n]
        ans[n] = sum
    }

    return ans
}

const ans = reverseSumArray([4,6,1,3,1,5])
console.log(ans)