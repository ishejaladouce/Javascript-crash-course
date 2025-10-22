// clean_jobs.js
const fs = require('fs');
const path = require('path');

// Input: the file you downloaded from Apify (rename it to apify_jobs.json)
const IN = path.join(__dirname, 'apify_jobs.json');
// Output: the file we will create with only the 4 fields
const OUT = path.join(__dirname, 'jobs_cleaned.json');

// Helper to clean extra spaces
function normalizeString(s) {
  if (!s) return null;
  return s.replace(/\s+/g, ' ').trim();
}

// Detect if a job is remote
function detectRemote(text = '') {
  return /\b(remote|work from home|hybrid|anywhere|distributed)\b/i.test(text);
}


const raw = JSON.parse(fs.readFileSync(IN, 'utf8'));


const jobs = raw.map(item => {
  const title = normalizeString(item.positionName || item.title || '');
  const company = normalizeString(item.company || '');
  const location = normalizeString(item.location || '');
  const textForRemote = `${title} ${company} ${location}`;

  return {
    title,
    company,
    location,
    isRemote: detectRemote(textForRemote) || /remote/i.test(location || '')
  };
});

// Save cleaned data
fs.writeFileSync(OUT, JSON.stringify(jobs, null, 2), 'utf8');
console.log(`Processed ${raw.length} jobs -> saved ${OUT}`);
