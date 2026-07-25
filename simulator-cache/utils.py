
def int_to_bin16(val: int) -> str:
    """Tam sayıyı 16-bit ikili string formatına dönüştürür (2's complement)."""
    val = val & 0xFFFF
    return f"{val:016b}"


def bin16_to_int(bin_str: str) -> int:
    """16-bit ikili string'i işaretli tam sayıya dönüştürür (2's complement)."""
    val = int(bin_str, 2)
    if val & 0x8000:  # En soldaki bit (MSB) 1 ise negatif
        val -= 0x10000
    return val


def alu(
    x: int,
    y: int,
    zx: int,
    nx: int,
    zy: int,
    ny: int,
    f: int,
    no: int,
) -> tuple[int, int, int]:
    """Hack ALU mantığını 6 kontrol biti ile simüle eder.

    Parametreler:
        x, y  : 16-bit tam sayı girdileri (-32768 .. 32767)
        zx    : Zero the x input?
        nx    : Negate the x input?
        zy    : Zero the y input?
        ny    : Negate the y input?
        f     : Function code: 1 for Add, 0 for And
        no    : Negate the output?

    Dönüş (out, zr, ng):
        out   : 16-bit ALU sonucu
        zr    : 1 ise out == 0
        ng    : 1 ise out < 0
    """
    # 16-bit maskeleme
    x = x & 0xFFFF
    y = y & 0xFFFF

    # 1. zx & nx işlemleri
    if zx:
        x = 0
    if nx:
        x = ~x & 0xFFFF

    # 2. zy & ny işlemleri
    if zy:
        y = 0
    if ny:
        y = ~y & 0xFFFF

    # 3. f fonksiyonu (1: Add, 0: And)
    if f:
        out = (x + y) & 0xFFFF
    else:
        out = (x & y) & 0xFFFF

    # 4. no mantığı
    if no:
        out = ~out & 0xFFFF

    # İkiye tümleyen işaretli tamsayı değerini al
    signed_out = bin16_to_int(f"{out:016b}")

    # Bayraklar (Flags)
    zr = 1 if out == 0 else 0
    ng = 1 if signed_out < 0 else 0

    return signed_out, zr, ng


def run_18_alu_operations(x: int, y: int) -> dict:
    """Nand2Tetris spesifikasyonundaki 18 temel ALU operasyonunu çalıştırır."""
    operations = {
        "0": (1, 0, 1, 0, 1, 0),
        "1": (1, 1, 1, 1, 1, 1),
        "-1": (1, 1, 1, 0, 1, 0),
        "x": (0, 0, 1, 1, 0, 0),
        "y": (1, 1, 0, 0, 0, 0),
        "!x": (0, 0, 1, 1, 0, 1),
        "!y": (1, 1, 0, 0, 0, 1),
        "-x": (0, 0, 1, 1, 1, 1),
        "-y": (1, 1, 0, 0, 1, 1),
        "x+1": (0, 1, 1, 1, 1, 1),
        "y+1": (1, 1, 0, 1, 1, 1),
        "x-1": (0, 0, 1, 1, 1, 0),
        "y-1": (1, 1, 0, 0, 1, 0),
        "x+y": (0, 0, 0, 0, 1, 0),
        "x-y": (0, 1, 0, 0, 1, 1),
        "y-x": (0, 0, 0, 1, 1, 1),
        "x&y": (0, 0, 0, 0, 0, 0),
        "x|y": (0, 1, 0, 1, 0, 1),
    }

    results = {}
    for op_name, ctrl_bits in operations.items():
        zx, nx, zy, ny, f, no = ctrl_bits
        out, zr, ng = alu(x, y, zx, nx, zy, ny, f, no)
        results[op_name] = {"out": out, "zr": zr, "ng": ng}

    return results