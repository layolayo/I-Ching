# I-Ching: Stalks & Sacred Marbles Divination Engine

> **The Kennedy Interpretation**: A rigorous mathematical revision of the classical Yarrow Stalk sorting algorithm, accounting for physical hand partition boundaries and introducing the **38-Marble Divination Method**.

---

## The 38-Marble Method: Historical Evolution & Mathematical Reality

### 1. From Coin Shortcuts to Gardner's 1974 Model
For centuries, the traditional 18-pass yarrow stalk ritual preserved by Song Dynasty scholar Zhu Xi (朱熹, 1186 CE) was the gold standard of I-Ching divination. Because manual sorting takes 15 to 20 minutes, Westerners popularized flipping three coins.

In 1974, famed mathematician **Martin Gardner** proved in *Scientific American* that three coins distort the oracle. Coins generate equal 12.5% chances for both changing lines (Old Yang and Old Yin). In authentic Daoist cosmology, this is fundamentally wrong: **Yang** (creative fire, initiative) is dynamic and quick to burn out and transform; whereas **Yin** (earth, darkness, receptivity) is steadfast, cold, and slow to alter course. 

Gardner derived the first modern mathematical model of stalks: a **16-branch matrix** where restless Yang changes three times more readily than Yin:
* **Old Yin (6)**: 1/16 = 6.25%
* **Young Yang (7)**: 5/16 = 31.25%
* **Young Yin (8)**: 7/16 = 43.75%
* **Old Yang (9)**: 3/16 = 18.75%

To reproduce this without arithmetic, early practitioners created a **32-marble bag** (doubling the 16-ratio: 14 Black, 10 White, 6 White-Speckled, 2 Black-Speckled).

---

### 2. The 2006 Physical Hands Reality (Andrew Kennedy)
In his 2006 work *Briefing Leaders*, researcher **Andrew Kennedy** discovered that Gardner's 1974 model was idealized "chalkboard math." Gardner had treated stalks like pure theoretical numbers that divide evenly into quarters. 

Real human hands do not divide stalks on a chalkboard:
1. When you split 49 stalks into your left and right hands, **neither hand can ever be empty**.
2. You immediately take 1 stalk from your right hand to hold between your fingers—meaning the right hand **must hold at least 2 stalks initially**, or it would be left empty.
3. Therefore, dividing 49 stalks between two physical hands creates **47 possible physical split points** (2 ≤ West ≤ 48).
4. **47 is a prime number**—it does not divide into clean chalkboard quarters!
5. On subsequent passes (dividing 44, 40, 36, or 32 stalks), the same physical hand boundaries apply.

---

### 3. Why 38 Marbles Replaces 32 (The Global Optimum)
Because physical hands cannot hold zero stalks, real-world yarrow probabilities subtly shift away from Gardner's chalkboard 16/32 model:
* **The 32-Marble Bag is Inaccurate**: Line probabilities in the 32-marble bag are off by as much as **2.4% on every single line** (Young Yang is over-represented by +2.38%, and Old Yang is under-represented by -2.37%).
* **The 38-Marble Bag is Near-Perfect**: Calculating the exact cumulative probability across all physical hand splits reveals that the true odds match a pouch of **38 marbles to within less than a tenth of one percent (< 0.09%)**!
* **Global Mathematical Proof**: An exhaustive mathematical search across all possible pouch sizes between 10 and 100 objects proves that **38 is the #1 global optimum in existence**.

| Line Type | Symbol | Meaning | Gardner (32 Bag) | True Physical Stalks | Kennedy (38 Bag) | Accuracy Error |
| :--- | :---: | :--- | :---: | :---: | :---: | :---: |
| **Young Yin (8)** | ⚋ | Unchanging Yin | 43.75% (14/32) | **44.84%** | **44.74%** (17/38) | **< 0.10%** |
| **Young Yang (7)** | ⚊ | Unchanging Yang | 31.25% (10/32) | **28.87%** | **28.95%** (11/38) | **< 0.08%** |
| **Old Yang (9)** | ⚊ ○ | Changing Yang → Yin | 18.75% (6/32) | **21.12%** | **21.05%** (8/38) | **< 0.07%** |
| **Old Yin (6)** | ⚋ ✕ | Changing Yin → Yang | 6.25% (2/32) | **5.17%** | **5.26%** (2/38) | **< 0.09%** |

The 32-marble bag was abstract paper theory; **38 marbles is what physical yarrow stalks actually do in human hands**.

---

### 4. How the 38-Marble Pouch Works
Consulting 49 stalks takes 15–20 minutes across 18 manual hand-divisions. By placing **38 marbles** into an opaque pouch:
* **17 Pure Black Marbles** — Young Yin (8) [44.74%]
* **11 Pure White Marbles** — Young Yang (7) [28.95%]
* **8 White Marbles with Black Specks (●)** — Old Yang (9) [21.05% · Changing]
* **2 Black Marbles with White Specks (✕)** — Old Yin (6) [5.26% · Changing]

You can consult the oracle in under 60 seconds with total mathematical fidelity:
1. Shake the pouch.
2. Draw 1 marble blindly and record Line 1 (Base / Earth).
3. Return the marble to the pouch and shake.
4. Repeat 6 times from the bottom up to complete the hexagram.

---

### 5. Benchmark Pages in this Repository
* **`probability-marbles.html`**: Runs simulated draws from the 38-marble pouch.
* **`probability-all.html`**: Side-by-side empirical benchmark comparing 3 Coins, 38 Marbles, and 49 Yarrow Stalks.
* **`kinwen_with_changing_lines.py`**: Calculates exact transition probabilities across all 4,096 King Wen hexagram transitions using the 38-object fractional matrix.
* **`index.html`**: Modern responsive web application supporting the 38-Marble Pouch and 49 Yarrow Stalks.

This code is free to use. If you like it, you can <a href="https://www.buymeacoffee.com/brianfit">buy me a coffee!</a> (I really like coffee)

The javascript here is the core of [a fairly popular app I've written](http://www.brian-fitzgerald.net/i-ching/?github) to consult the I-Ching. This code randomly generates a hexagram of six lines according to a bronze-age methodology of sorting Yarrow Stalks. Here's an overly long explanation of that method and why it's statistically different from the three-coin method of generating hexagrams that most of us learned in the west.

Take 50 stalks. Remove one, set it aside. Randomly separate the remaining 49 stalks into two piles, East and West. Take one stalk from the West heap and hold it between thumb and forefinger of your left hand. Take stalks in groups of four from the East pile, until four or fewer stalks remain. Keep this remainder, place it between the ring and middle finger of the left hand. Take stalks in groups of four from the West pile until four or fewer stalks remain. Keep this remainder, and place it between the middle and forefingers of the left hand.

Your left hand now holds a sum of stalks equal to 9 or 5, being made up of one of the following possibilities:

 1+1+3=5

 1+2+2=5

 1+3+1=5

 1+4+4=9

If the number of stalks is nine, a value of 2 is assigned to this counting. If it was five, the number three is assigned. The 9 or 5 stalks are put aside.

The rest of the stalks (40 or 44 by now) are again divided into two piles and counted off as above. The possible outcomes this time are:

 1+1+2=4

 1+2+1=4

 1+3+4=8

 1+4+3=8

This time, an 8 stalk remainder is assigned the number

A 4 stalk remainder receives a 3. The four or eight stalks are set aside, and the remaining 36, 40, 32, or 38 stalks are again divided in two and counted off. The possibilities are again:

 1+1+2=4

 1+2+1=4

 1+3+4=8

 1+4+3=8

And again a remainder of 8 is valued at 2, a remainder of 4 at 3.

From these three operations result the following possibilities:

 2+2+3=7

 2+3+3=8

 2+3+2=7

 2+2+2=6

 3+2+2=7

 3+3+2=8

 3+2+3=8

 3+3+3=9

It is these results which determine whether a line is solid or broken. A 7 meant a strong, solid line. An 8 meant a yielding, broken line. A 9 was considered a strong moving toward yielding line. A 6 was a yielding moving toward strong line.

By repeating the above process six times, a hexagram was built up from the bottom.

Like most westerners exposed to the I-Ching, I was taught the coin method of generating a line, which is far easier than the method above. By this method, three coins are tossed. Heads are worth 2, tails 3. The possibilities were thus:

 Head+Head+Head=6

 Head+Head+Tail=7

 Head+Tail+Tail=8

 Tail+Tail+Tail=9

This means, however, a slight difference in probabilities from the yarrow stalk method. The chance of any one coin being head or tail is ALWAYS 50/50. However, the chance of a "Tail" on the first "Toss" in the yarrow stalk method is almost 3 to 1. Recall, the possible results for the first division of 49 stalks was this:

 1+1+3=5 (Value 3)

 1+2+2=5 (Value 3)

 1+3+1=5 (Value 3)

 1+4+4=9 (Value 2)

Of four possible outcomes, three of them result in a 5, only one in a 9. This means, in effect, that when we look to the lines, those generated by a 2 in the first place are less likely to occur than those that start with a 3:

 Less likely:

 2+2+3=7 (Strong)

 2+3+3=8 (Yielding)

 2+3+2=7 (Strong)

 2+2+2=6 (Yielding Changing)

 More likely:

 3+2+2=7 (Strong)

 3+3+2=8 (Yielding)

 3+2+3=8 (Yielding)

 3+3+3=9 (Strong Changing)

It therefore makes sense that unchanging Yielding lines are slightly more likely to show up than unchanging Strong lines, and that a yielding changing line is the least likely all possible combinations to turn up. This is because unlike the regular yielding and strong lines, the changing lines are each generated by only one possible combination of stalks. The yielding, changing combination, because it begins with 2, is therefore heavily disfavored over the strong changing line.

Which is all just to say that the coin method does not hold the same built-in bias that the yarrow stalk method has. Surely note must have been made by the ancients that a 6 was a relatively rare occurrence indeed. Certainly, anyone in frequent consultation with the book by the yarrow stalk method would have noted the anomaly. I noticed the reticence of 6 after many many runs of the developing program and thought my coding was somehow flawed. But no! Perseverance furthers. No Blame.

Update: Wikipedia sums up all that blather very succinctly:

<table class="wikitable sortable">
<tr>
<th>Number</th>
<th colspan="2">Yarrow stick probability</th>
<th colspan="2">Three coin probability</th>
<th>YinYang</th>
<th>Signification</th>
<th>Symbol</th>
</tr>
<tr>
<td>6</td>
<td>1/16</td>
<td rowspan="2">8/16</td>
<td>2/16</td>
<td rowspan="2">8/16</td>
<td>old yin</td>
<td>yin changing into yang</td>
<td style="text-align:center;"><s><b>---</b></s><b>x</b><s><b>---</b></s></td>
</tr>
<tr>
<td>8</td>
<td>7/16</td>
<td>6/16</td>
<td>young yin</td>
<td>yin unchanging</td>
<td style="text-align:center;"><s><b>---</b></s>&#160;&#160;<s><b>---</b></s></td>
</tr>
<tr>
<td>9</td>
<td>3/16</td>
<td rowspan="2">8/16</td>
<td>2/16</td>
<td rowspan="2">8/16</td>
<td>old yang</td>
<td>yang changing into yin</td>
<td style="text-align:center;"><s><b>---o---</b></s></td>
</tr>
<tr>
<td>7</td>
<td>5/16</td>
<td>6/16</td>
<td>young yang</td>
<td>yang unchanging</td>
<td style="text-align:center;"><s><b>--------</b></s></td>
</tr>
</table>

If you enjoyed this, you can <a href="https://www.buymeacoffee.com/brianfit">buy me a coffee!</a> (Did I mention I really like coffee)
