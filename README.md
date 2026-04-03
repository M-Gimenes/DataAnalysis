# Student Dropout Analysis in Higher Education

An end-to-end data analysis project investigating the patterns and factors behind academic attrition at a Brazilian higher education institution. The work combines exploratory data analysis, statistical visualization, and geospatial mapping to turn raw enrollment records into actionable insight.

---

## What this project explores

Student dropout is one of the most costly and least visible problems in higher education. This project digs into a real enrollment dataset to answer questions like:

- Which courses have the highest dropout rates?
- At what point in the degree do most students leave?
- How do dropout patterns differ across gender, race/ethnicity, family income, and school of origin?
- Where do dropout students come from geographically?

---

## Key findings

- Dropout is heavily concentrated in the **first two semesters**, suggesting that early intervention is where institutions should focus.
- Dropout rates vary significantly across courses, with some programs losing a disproportionate share of students.
- Students from **public high schools** account for the majority of dropouts in most courses.
- Geographic clustering of dropout students is visible in heatmaps centered on the Cachoeiro de Itapemirim region.

---

## Skills demonstrated

| Area                         | Tools                             |
| ---------------------------- | --------------------------------- |
| Data wrangling               | `pandas`                        |
| Statistical visualization    | `matplotlib`                    |
| Geospatial analysis          | `folium`, `geopy` (Nominatim) |
| CEP → coordinates geocoding | custom utility in `src/`        |
| Exploratory analysis         | Jupyter Notebooks                 |

---

## Project structure

```
DataAnalysis/
├── notebooks/
│   ├── análise.ipynb      # Core EDA: dropout by course, year, semester, demographics
│   └── gráficos.ipynb     # Chart generation for all visual outputs
├── src/
│   └── coordenadas.py     # Geocoding utility: CEP → (lat, lon) via Nominatim
└── outputs/
    ├── figures/           # Static charts (PNG)
    └── maps/              # Interactive HTML maps (Folium)
```

---

## Visualizations

The `outputs/` folder contains the full set of generated assets:

**Charts**

- Dropout rate by course (pie)
- Dropout volume over time — yearly trend (line)
- Semesters completed before dropping out (histogram)
- Dropout by gender per course
- Family income distribution by course
- School of origin (public vs. private) of dropout students
- Racial/ethnic composition of dropouts per course
- Proportion of dropouts relative to total enrollment per area

**Interactive maps**

- Point map and heatmap of the full dataset
- Point map and heatmap focused on Cachoeiro de Itapemirim

---

## Context

This project was developed as a personal research initiative to better understand the dropout phenomenon at a federal institution in Espírito Santo, Brazil. The goal was not only technical — it was to make a real social problem more legible through data.
