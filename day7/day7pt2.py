from tqdm import tqdm


def has_valid_op_seq(n: int, seq: list[str], cur: int) -> int:
    """check if remaining values in the sequence can equal n by using + and *

    Args:
        n (int): target value
        seq (str]): remaining operands
        cur (int): value after last operation

    Returns:
        int: 1 if sequence is valid or 0 if false
    """
    if len(seq) == 0:
        return 1 if n == cur else 0
    else:
        # calculated the result of the equation if a *, +, or || is used
        plus_op = cur + int(seq[0])
        # protect from multiplying by zero
        if cur == 0:
            cur = 1
        mul_op = cur * int(seq[0])
        concat_op = int(str(cur) + seq[0])

        plus_val = has_valid_op_seq(n=n, seq=seq[1:], cur=plus_op)
        mul_val = has_valid_op_seq(n=n, seq=seq[1:], cur=mul_op)
        concat_val = has_valid_op_seq(n=n, seq=seq[1:], cur=concat_op)

        return plus_val + mul_val + concat_val


with open("input7.txt") as f:
    lines = f.read().splitlines(keepends=False)

total = 0
for line in tqdm(lines, "calculating"):
    snums = line.split(" ")

    n = int(snums[0][:-1])  # throw out trailing ':
    seq = snums[2:]
    cur = int(snums[1])
    num_s = has_valid_op_seq(n=n, seq=seq, cur=cur)
    # print(f"{num_s} solutions in {line}")

    if num_s > 0:
        # add the equation's result to the running total
        total += int(snums[0][:-1])
print(total)
