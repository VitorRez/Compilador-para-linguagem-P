fn sub(x: int, y: int) -> int {
    return x - y;
}


fn fibonacci(n: int) -> int {
    if n == 0 {
        return 0;
    }
    else if n == 1 {
        return 1;
    }
    else {
        return fibonacci(sub(n, 1)) + fibonacci(n, 2);
    }
}

fn main() {
    let num: int;
    num = 10;
    println("{}", fibonacci(num));
}