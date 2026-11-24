"""One-sentence satirical roast for make.fun bounty
u-swift-raven-16-the-long-roast-lawmakers-and-the-f3a3bdf7 (variant C:
THE RULE THEY WROTE).

Writes the roast to /output/entry.txt FIRST, then best-effort writes the
same bytes to entry.txt in the repo root (the grader sandbox repo root may
be read-only -- that write must never crash the program).
"""

import os

ENTRY = (
    "The lawmaker who authored the Mandatory PDF Filing Act signed it into "
    "law on live television, then filed his own disclosure form as a Pages "
    "file, watched his own portal bounce it three times for unsupported "
    "format, and asked the twenty-year-old intern who earns twelve dollars "
    "an hour to convert it into a PDF for him."
)


def main() -> None:
    text = ENTRY
    assert 1 <= len(text) <= 320, f"length {len(text)} outside 1-320"
    assert text == text.strip(), "leading/trailing whitespace"
    assert "  " not in text, "double space"
    assert text.count(".") == 1 and text.endswith("."), "must be one sentence"
    assert ". " not in text, "no sentence break inside entry"
    assert "?" not in text and "!" not in text, "no other sentence terminator"
    assert "\n" not in text, "no newline inside entry"

    data = text.encode("utf-8")
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "wb") as f:
        f.write(data)

    repo_root = os.path.join(os.path.dirname(os.path.abspath(__file__)),
                             "entry.txt")
    try:
        with open(repo_root, "wb") as f:
            f.write(data)
    except OSError:
        pass

    with open("/output/entry.txt", "rb") as f:
        assert f.read() == data, "read-back mismatch"

    import hashlib

    print(f"wrote /output/entry.txt: {len(text)} chars, "
          f"sha256={hashlib.sha256(data).hexdigest()}")


if __name__ == "__main__":
    main()
