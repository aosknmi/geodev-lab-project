# Month 1 Summary

## Question

Which areas in Oyo State fall outside a 5 km buffer zone around health facilities?

## Operation Used

I used the **Buffer** operation to create a 5 km buffer zone around health facilities in Oyo State. I chose the Buffer operation because it directly addresses part of the question by showing the areas within 5 km of health facilities and, consequently, helping to identify the areas that fall outside the coverage zone.

I also used the **Dissolve** operation to combine overlapping buffer zones and the **Difference** operation to identify the parts of Oyo State that fall outside the combined 5 km buffer zones.

## What I Expected and What I Got

I expected the 5 km buffer analysis to show the areas of Oyo State that are within and outside the 5 km coverage zone of health facilities.

The result matched my expectation. The analysis showed that approximately **10,265.3 km²**, representing **37.19%** of Oyo State's total area of **27,603.42 km²**, falls outside the combined 5 km buffer zones. The remaining **62.81%** of the state's land area falls within these zones.

This indicates that a substantial portion of Oyo State is located more than 5 km in straight-line distance from the nearest mapped health facility.

## What Surprised Me

The analysis showed that approximately **37.19% of Oyo State's land area** falls outside the 5 km coverage zones of the mapped health facilities. This indicates that some areas may be relatively far from the nearest mapped health facility and highlights the importance of spatial analysis in identifying potential gaps in healthcare coverage.

However, being outside a 5 km buffer does not necessarily mean that an area has no access to healthcare. The analysis measures straight-line proximity rather than actual road travel distance, facility capacity, or the number of people affected.

## What Data I Still Need

To better understand the areas outside the 5 km coverage zone, I would need additional data such as:

- **Population data:** To estimate the number of people living within and outside the coverage zones.
- **Settlement and community locations:** To identify specific communities located beyond the 5 km buffer zones.
- **Health facility capacity and available services:** To determine whether existing facilities can adequately serve nearby populations.
- **More complete and up-to-date health facility data:** To improve the reliability of the coverage analysis.

These additional datasets would help provide more context about the population potentially affected and accessibility to health facilities in areas outside the 5 km buffer zones.
