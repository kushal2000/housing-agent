# Housing Search Profile
Last updated: 2026-04-06

## Who
- **Kushal Kedia** — Incoming MIT postdoc (CSAIL/LIDS), starting June 15, 2026
- **Girlfriend** — Working at Cannon Design, downtown Boston (Financial District area)
- Looking to live together in a studio or 1BR

## Hard Filters (auto-reject if ANY violated)
- Price: $1,500 - $3,500/month
- Bedrooms: Studio or 1BR only
- Available: May 15 - July 1, 2026 (flexible 2 weeks either side of June 15)
- Location: Must be within 30 min transit to MIT (77 Massachusetts Ave, Cambridge)
- NO: shared rooms, roommate-wanted-only posts, short-term (<6 months)

## Scoring Axes (each 1-5)

### MIT Commute (weight: 3x)
- 5: Walking distance (<15 min walk to MIT campus)
- 4: One T stop or short bike (<10 min Red Line / bus)
- 3: 15-25 min transit (Davis, Porter, Central, Kendall, Harvard)
- 2: 25-40 min transit (Somerville outskirts, Allston, Back Bay)
- 1: 40+ min or requires transfer

### Downtown Boston Commute (weight: 2x)
- 5: <20 min to Financial District/Seaport (Red Line direct)
- 4: 20-30 min (one transfer or longer Red Line)
- 3: 30-40 min
- 2: 40-50 min
- 1: 50+ min

### Price (weight: 2x)
~$3,000/month is the realistic market rate for a 1BR near MIT. Score accordingly.
- 5: Under $2,400 (great deal)
- 4: $2,400 - $2,800
- 3: $2,800 - $3,100 (realistic / expected)
- 2: $3,100 - $3,300
- 1: $3,300 - $3,500

### Quality Signals (weight: 1x)
Start at 3, then adjust:
- +1: In-unit or in-building laundry
- +1: Heat/hot water included
- +1: No broker fee
- +1: Hardwood floors, natural light, updated kitchen/bath
- -1: Basement/garden level
- -1: No photos or vague description (possible scam)
- Cap at 5, floor at 1

### Move-in Date Fit (weight: 1x)
- 5: June 1-15 available
- 4: June 16-30 or May 15-31
- 3: July 1
- 2: August 1
- 1: September 1+

## Composite Score
Score = (MIT_commute * 3 + Downtown_commute * 2 + Price * 2 + Quality * 1 + DateFit * 1) / 4.5
Normalized to 10-point scale (multiply by 10/45 * 9, then add 1... simplified: just use the weighted sum / 4.5 and round to 1 decimal).

Max possible = 45/4.5 = 10.0
Min possible = 9/4.5 = 2.0

## Alert Thresholds
- **URGENT (score >= 8.0)**: Send email immediately + auto-outreach
- **GOOD (score 6.0-7.9)**: Include in digest email + auto-outreach
- **MEH (score 4.0-5.9)**: Log only, no email, no outreach
- **REJECT (score < 4.0)**: Discard

## Neighborhood Tier Map (for commute scoring without maps API)

### MIT Commute Tiers
- **Tier 1 (score 5)**: Cambridgeport, Kendall Square, MIT campus area, Central Square, Area 4
- **Tier 2 (score 4)**: Harvard Square, Inman Square, East Cambridge, East Somerville, Wellington-Harrington
- **Tier 3 (score 3)**: Davis Square, Porter Square, Union Square Somerville, Winter Hill, Mid-Cambridge
- **Tier 4 (score 2)**: Allston, Brighton, Back Bay, South End, Charlestown, Medford
- **Tier 5 (score 1)**: Dorchester, Roxbury, Jamaica Plain, Brookline (far end), Malden

### Downtown Boston Commute (Red Line access is key)
- **On Red Line (score 4-5)**: Kendall, Central, Harvard, Porter, Davis → Park St / Downtown Crossing direct
- **Near Red Line (score 3-4)**: Inman, East Somerville, Cambridgeport (walk to Red Line)
- **Transfer needed (score 2-3)**: Allston (Green→Red), Back Bay (Orange→Red), Charlestown (bus)
- **Far (score 1-2)**: Medford, Malden, outer Somerville

## Scam Detection Flags
Flag (do NOT auto-outreach) if any of these are present:
- Price dramatically below market (studio in Cambridge for under $1,200)
- No photos or only stock/generic photos
- "Send deposit before viewing" or "wire transfer"
- Out-of-state or out-of-country landlord who can't show in person
- Duplicate listing text appearing at multiple addresses
- Too-good-to-be-true amenities for the price
