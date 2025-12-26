# LeetCode Card Alternatives

## Option 1: LeetCode Badge (Static & Reliable)
```markdown
[![LeetCode user icycoldveins](https://img.shields.io/badge/dynamic/json?style=for-the-badge&labelColor=black&color=%23ffa116&label=Solved&query=solvedOverTotal&url=https%3A%2F%2Fleetcode-badge.vercel.app%2Fapi%2Fusers%2Ficycoldveins&logo=leetcode&logoColor=yellow)](https://leetcode.com/icycoldveins/)
```

## Option 2: KnlnKS LeetCode Stats (Alternative Service)
```markdown
![LeetCode Stats](https://leetcode-stats.vercel.app/api?username=icycoldveins&theme=dark)
```

## Option 3: Self-Hosted Solution
Use GitHub Actions to generate and commit a static image:
```yaml
name: Update LeetCode Stats
on:
  schedule:
    - cron: '0 0 * * *'  # Daily update
  workflow_dispatch:

jobs:
  update-readme:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v2
      - name: LeetCode Readme Stats
        uses: madushadhanushka/github-readme-leetcode-stats@v1.0.0
        with:
          LEETCODE_USERNAME: icycoldveins
```

## Option 4: Manual Screenshot
Take a screenshot of your LeetCode profile and commit it as a static image:
```markdown
![LeetCode Stats](./leetcode-stats.png)
```

## Option 5: Text-Based Stats (Never Fails)
```markdown
### 📊 LeetCode Stats
- **Problems Solved:** 150+
- **Contest Rating:** 1800+
- **Languages:** Python, JavaScript, Java
- [View Profile →](https://leetcode.com/icycoldveins/)
```

## Recommended Approach
Combine static badges with fallback text:
```markdown
<!-- Primary: Try dynamic card -->
![LeetCode Stats](https://leetcard.jacoblin.cool/icycoldveins?theme=dark&font=source_code_pro&ext=heatmap)

<!-- Fallback: If card doesn't load, show badge -->
[![LeetCode](https://img.shields.io/badge/LeetCode-Profile-FFA116?style=for-the-badge&logo=leetcode)](https://leetcode.com/icycoldveins/)
```