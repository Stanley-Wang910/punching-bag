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
