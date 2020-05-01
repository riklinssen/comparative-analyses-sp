# SP - Comparative analyses - 2020

Code to reproduce analyses and visuals for Strategic Partnership Comparative Analyses 2020 published here <add link> --> add link to report here. 

# Technologies
Project is created with: 
- STATA 13.1
- Python 3.8.0 

# Structure
```
├───docs                    <- data documentation, questionnaire other relevant docs
│   
├───notebooks               <-notebooks for EDA, code snippets etc. 
│   
│      
│      
│      
│   
└───src                     <-.do (cleaning & PSM models (STATA) .py (visualisations) 
    ├───data                 
    │   ├───clean           <-Final datasets used for report generation  
    │   ├───interim         <-intermediate data that has been transformed 
    │   └───raw             <-original data dump         
    └───graphs              <-visualisations in report 
```
# Structure

```
├───Data
│   ├───Clean           <-- Final datasets used for report generation  
│   ├───Intermediate    <-- Intermediate datasets
│   ├───Output          <-- Output data (e.g. resultssets generated through STATA)
│   └───Raw             <-- (Links to) Original data used for comparative analyses (on box)
├───Docs                <-- (links to) data documentation, questionnaires other relevant docs (on Box)
├───src                 
└───Visualisations      <-- Graphs other visualisations
```
