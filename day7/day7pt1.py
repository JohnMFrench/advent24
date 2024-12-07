from tqdm import tqdm


# check if the sequence has a valid order of operations
def has_valid_op_seq(n: int, seq: list[str], cur: int) -> bool:
    """check if remaining values in the sequence can equal n by using + and *

    Args:
        n (int): target value
        seq (str]): remaining operands
        cur (int): value after last operation

    Returns:
        bool: whether sequence is valid
    """
    if len(seq) == 0:
        return 1 if n == cur else 0
    else:
        plus_op = cur + int(seq[0])
        if cur == 0:
            cur = 1
        mul_op = cur * int(seq[0])
        # test if sequence is valid with + as next operator
        plus_val = has_valid_op_seq(n=n, seq=seq[1:], cur=plus_op)
        mul_val = has_valid_op_seq(n=n, seq=seq[1:], cur=mul_op)
        return plus_val + mul_val
        # test if sequence is valid with * as next operator


# print(has_valid_op_seq(n=190, seq=['10', '19'], cur=0))
# print(has_valid_op_seq(n=191, seq=['10', '19'], cur=0))
print(has_valid_op_seq(n=190, seq=["19"], cur=10))
print(has_valid_op_seq(n=191, seq=["10", "19"], cur=0))


print(has_valid_op_seq(n=3267, seq=["81", "40", "27"], cur=0))
print(has_valid_op_seq(n=3237, seq=["81", "40", "27"], cur=0))

with open("input7.txt") as f:
    lines = f.read().splitlines(keepends=False)

num_combos = 0
total = 0
for line in tqdm(lines, "calculating"):
    snums = line.split(" ")
    n = int(snums[0][:-1])  # throw out trailing ':
    seq = snums[2:]
    cur = int(snums[1])
    num_s = has_valid_op_seq(n=n, seq=seq, cur=cur)
    print(f"{num_s} solutions in {line}")
    num_combos += num_s
    if num_s > 0:
        total += int(snums[0][:-1])
print(total)
# print(num_combos)
