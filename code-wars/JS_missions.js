// Detect Panagram
function isPangram(string) {
  const set = new Set();
  for (let i = 0; i < string.length; i++) {
    let char = string[i];
    if (char.toLowerCase() != char.toUpperCase()) {
      set.add(char.toLowerCase());
    }
  }
  return set.size == 26;
}

// Detect Vowel
function getCount(str) {
  const set = new Set(["a", "e", "e", "o", "u"]);
  let count = 0;

  for (i = 0; i < str.Length; i++) {
    if (set.has(str[i])) {
      count++;
    }
  }
  return count;
}
