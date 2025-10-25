### Assessor Script Configuration

-----

### 1\. Create and Populate `config.json`

Create a file named **`config.json`** in your project's root directory with the following structure:

```json
{
  "login": "login",
  "password": "login",
  "assessor": {
    "retries": 1000000,
    "short_pause_sec": 1,
    "long_pause_sec": 1,
    "pools": [11],
    "fos_id": "11"
  }
}
```

### 2\. Update Credentials

Change the placeholder values:

* **`"login"`:** Your actual username or email.
* **`"password"`:** Your actual password.

### 3\. Discover Project Parameters

The values for `"fos_id"` and `"pools"` must be specific to your current **Project** (e.g., "Marathon," "Track C").

To find these values:

1.  Open your browser's **Developer Tools** (F12) and go to the **Network** tab.
2.  Trigger the request by clicking the **"Request"** button on the website.
3.  Examine the initiated `/api/assessments/request` call:
    * **`fos_id`:** Found in the **Request Headers**. This is the unique identifier for your **Project/Course Group**.
    * **`pools`:** Found in the **Request Payload** (the body of the request). This is the ID for the **specific task category** you are requesting an assessment for.

*(Correction: You are correct; a Project is a group of tasks. The `fos_id` scopes the request to that Project, and `pools` selects the specific subset of tasks within it.)*