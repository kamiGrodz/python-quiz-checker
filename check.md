# WordPress Privacy & Security Hardening Guide

## 1. Step-by-Step WordPress Hardening Guide

### Phase 1: Initial Setup
1. **Fresh Installation**
   - Use latest WordPress version
   - Choose strong admin username (never "admin")
   - Generate complex password (20+ characters)
   - Use unique email for admin account

2. **File Permissions Setup**
   ```bash
   # Set correct permissions
   find /path/to/wordpress -type d -exec chmod 755 {} \;
   find /path/to/wordpress -type f -exec chmod 644 {} \;
   chmod 600 wp-config.php
   ```

3. **Database Security**
   - Change table prefix from default `wp_` to something unique (e.g., `mysite_`)
   - Create dedicated database user with minimal privileges
   - Use strong database password

4. **Core Configuration (wp-config.php)**
   ```php
   // Security keys - generate from WordPress.org
   define('AUTH_KEY', 'your-unique-key');
   // ... add all 8 security keys
   
   // Security settings
   define('DISALLOW_FILE_EDIT', true);
   define('AUTOMATIC_UPDATER_DISABLED', true);
   define('WP_AUTO_UPDATE_CORE', false);
   define('FORCE_SSL_ADMIN', true);
   define('WP_DEBUG', false);
   
   // Hide errors from public
   ini_set('display_errors', 0);
   ```

### Phase 2: Server Configuration
5. **SSL/HTTPS Setup**
   - Install SSL certificate
   - Force HTTPS redirects
   - Update WordPress URL settings

6. **User Management**
   - Remove default admin user if created
   - Use principle of least privilege
   - Enable two-factor authentication

### Phase 3: Plugin Installation
7. **Install Wordfence Security** (detailed below)
8. **Remove unnecessary plugins/themes**
9. **Regular security audits**

## 2. Wordfence Security - Complete Guide

### What is Wordfence?
Wordfence is a comprehensive WordPress security plugin that provides:
- Web Application Firewall (WAF)
- Malware scanner
- Login security
- Traffic analysis
- Threat intelligence

### Installation & Setup
1. **Install Plugin**
   - Go to Plugins > Add New
   - Search "Wordfence Security"
   - Install and activate

2. **Initial Configuration**
   ```
   Wordfence > All Options
   ```

### Essential Wordfence Settings

#### Firewall Settings
- **Web Application Firewall Status**: Enabled and Optimized
- **Protection Level**: High
- **Real-time IP Blacklist**: Enabled
- **Malware IP Blacklist**: Enabled
- **Rate Limiting**: Enable (see rate limiting section)

#### Login Security
- **Brute Force Protection**: Enabled
- **Lock out after**: 5 failed attempts
- **Lock out duration**: 4 hours
- **Immediately lock out invalid usernames**: Enabled
- **Don't let WordPress reveal valid users**: Enabled

#### Scanner Settings
- **Scan frequency**: Daily
- **Scan file contents**: Enabled
- **Scan file permissions**: Enabled
- **Scan core files**: Enabled
- **Monitor disk space**: Enabled

#### Advanced Settings
- **Hide WordPress version**: Enabled
- **Disable pingbacks**: Enabled
- **Block fake Googlebots**: Enabled
- **Block malicious IPs**: Enabled

### Wordfence Maintenance
- Review alerts daily
- Update firewall rules weekly
- Run manual scans after updates
- Monitor traffic patterns monthly

## 3. No-Cookie Setup

Since you're not using cookies, configure:

### WordPress Settings
```php
// In wp-config.php - disable cookies where possible
define('COOKIE_DOMAIN', false);

// Remove cookie-related functions
remove_action('wp_head', 'wp_print_head_scripts', 9);
remove_action('wp_head', 'wp_enqueue_scripts', 1);
```

### Theme Configuration
- Remove any cookie consent banners
- Ensure no tracking cookies are set
- Audit third-party integrations

## 4. Secure Comment Management

### Comment Security Settings
1. **Discussion Settings** (Settings > Discussion):
   - Require registration to comment: Consider enabling
   - Close comments after X days: Enable (30 days recommended)
   - Require manual approval: Enable for new commenters
   - Comment moderation: Hold comments with 2+ links

2. **Anti-Spam Configuration**:
   ```php
   // Add to functions.php
   function secure_comment_form() {
       wp_nonce_field('comment_nonce', 'comment_nonce_field');
   }
   add_action('comment_form', 'secure_comment_form');
   ```

3. **Wordfence Comment Protection**:
   - Enable comment spam filtering
   - Set comment rate limiting
   - Block suspicious comment patterns

## 5. Server-Level Security Configurations

### Disable Directory Browsing
**What it means**: Prevents users from viewing directory contents when no index file exists.

#### Apache (.htaccess)
```apache
# Disable directory browsing
Options -Indexes

# Block access to sensitive files
<FilesMatch "\.(htaccess|htpasswd|ini|log|sh|inc|bak)$">
    Order Allow,Deny
    Deny from all
</FilesMatch>

# Protect wp-config.php
<files wp-config.php>
    order allow,deny
    deny from all
</files>

# Hide WordPress version
RewriteEngine On
RewriteRule ^wp-admin/install\.php$ - [F,L]
RewriteRule ^wp-admin/upgrade\.php$ - [F,L]
```

### Hide WordPress Version
#### Method 1: Functions.php
```php
// Remove version from head
remove_action('wp_head', 'wp_generator');

// Remove version from RSS feeds
add_filter('the_generator', '__return_empty_string');

// Remove version from scripts and styles
function remove_version_scripts_styles($src) {
    if (strpos($src, 'ver=')) {
        $src = remove_query_arg('ver', $src);
    }
    return $src;
}
add_filter('style_loader_src', 'remove_version_scripts_styles', 9999);
add_filter('script_loader_src', 'remove_version_scripts_styles', 9999);
```

### Rate Limiting Implementation

#### Wordfence Rate Limiting
```
Wordfence > Firewall > Rate Limiting:
- How many requests: 10
- Per time period: 1 minute
- Action: Throttle/Block
```

#### Server-Level (Nginx)
```nginx
# Add to server block
limit_req_zone $binary_remote_addr zone=login:10m rate=1r/s;
limit_req_zone $binary_remote_addr zone=wp:10m rate=10r/s;

location /wp-login.php {
    limit_req zone=login burst=2 nodelay;
}

location / {
    limit_req zone=wp burst=20 nodelay;
}
```

### Fail2Ban Configuration
#### Install Fail2Ban
```bash
# Ubuntu/Debian
sudo apt-get install fail2ban

# CentOS/RHEL
sudo yum install fail2ban
```

#### WordPress Jail Configuration
Create `/etc/fail2ban/jail.d/wordpress.conf`:
```ini
[wordpress]
enabled = true
filter = wordpress
logpath = /var/log/auth.log
maxretry = 3
bantime = 3600
findtime = 600

[wordpress-xmlrpc]
enabled = true
filter = wordpress-xmlrpc
logpath = /path/to/access.log
maxretry = 3
bantime = 3600
```

## 6. Remove WordPress Telemetry

### Core WordPress Telemetry Removal
```php
// Add to functions.php or mu-plugins

// Remove WordPress.org update checks
remove_action('wp_version_check', 'wp_version_check');
remove_action('wp_update_plugins', 'wp_update_plugins');
remove_action('wp_update_themes', 'wp_update_themes');

// Disable automatic updates communication
add_filter('automatic_updater_disabled', '__return_true');

// Remove update notifications
add_action('admin_menu', 'hide_admin_notices');
function hide_admin_notices() {
    remove_action('admin_notices', 'update_nag', 3);
}

// Disable pingbacks/trackbacks
add_filter('xmlrpc_enabled', '__return_false');
add_filter('pre_update_option_enable_xmlrpc', '__return_false');
add_filter('pre_option_enable_xmlrpc', '__return_zero');

// Remove DNS prefetch
remove_action('wp_head', 'wp_resource_hints', 2);

// Block external HTTP requests
add_filter('pre_http_request', 'block_external_requests', 10, 3);
function block_external_requests($preempt, $r, $url) {
    $allowed_domains = [
        'your-site.com',
        'api.wordpress.org' // Only if you need updates
    ];
    
    $host = parse_url($url, PHP_URL_HOST);
    if (!in_array($host, $allowed_domains)) {
        return new WP_Error('blocked', 'External request blocked');
    }
    return $preempt;
}

// Remove emoji scripts
remove_action('wp_head', 'print_emoji_detection_script', 7);
remove_action('wp_print_styles', 'print_emoji_styles');
remove_action('admin_print_scripts', 'print_emoji_detection_script');
remove_action('admin_print_styles', 'print_emoji_styles');
```

### Additional Privacy Settings
```php
// Disable user enumeration
add_action('init', 'block_user_enumeration');
function block_user_enumeration() {
    if (is_admin() || strpos($_SERVER['REQUEST_URI'], '/wp-json/') !== false) {
        return;
    }
    if (preg_match('/author=([0-9]*)/i', $_SERVER['QUERY_STRING'])) {
        die('Forbidden');
    }
}

// Remove WordPress meta tags
remove_action('wp_head', 'rsd_link');
remove_action('wp_head', 'wlwmanifest_link');
remove_action('wp_head', 'wp_shortlink_wp_head');
remove_action('wp_head', 'adjacent_posts_rel_link_wp_head');
```

## 7. Host Fonts Locally

### Step 1: Download Google Fonts
```bash
# Use google-webfonts-helper or download manually
# Example for Open Sans:
wget https://fonts.gstatic.com/s/opensans/v34/memSYaGs126MiZpBA-UvWbX2vVnXBbObj2OVZyOOSr4dVJWUgsjZ0C4nY1M2xLER.woff2
```

### Step 2: Store Fonts
```
/wp-content/themes/your-theme/fonts/
├── opensans-regular.woff2
├── opensans-bold.woff2
└── opensans-italic.woff2
```

### Step 3: CSS Implementation
```css
/* Add to style.css or create separate fonts.css */
@font-face {
    font-family: 'Open Sans';
    src: url('./fonts/opensans-regular.woff2') format('woff2');
    font-weight: 400;
    font-style: normal;
    font-display: swap;
}

@font-face {
    font-family: 'Open Sans';
    src: url('./fonts/opensans-bold.woff2') format('woff2');
    font-weight: 700;
    font-style: normal;
    font-display: swap;
}
```

### Step 4: Remove Google Fonts
```php
// Remove Google Fonts from themes/plugins
function remove_google_fonts() {
    wp_deregister_style('google-fonts');
    wp_dequeue_style('google-fonts');
}
add_action('wp_enqueue_scripts', 'remove_google_fonts', 20);
```

## 8. Stay Updated - Maintenance Strategy

### Automated Monitoring Setup
```php
// Create /wp-content/mu-plugins/update-monitor.php
function check_for_updates() {
    $updates = get_site_transient('update_core');
    $plugin_updates = get_site_transient('update_plugins');
    $theme_updates = get_site_transient('update_themes');
    
    if (!empty($updates->updates) || !empty($plugin_updates->response) || !empty($theme_updates->response)) {
        // Send notification email
        wp_mail(get_option('admin_email'), 'Updates Available', 'WordPress updates available.');
    }
}
add_action('wp_loaded', 'check_for_updates');
```

### Manual Update Checklist
#### Daily Tasks:
- [ ] Check Wordfence alerts
- [ ] Review security logs
- [ ] Monitor failed login attempts

#### Weekly Tasks:
- [ ] Check for core updates
- [ ] Review plugin updates
- [ ] Check theme updates
- [ ] Backup site before updates

#### Monthly Tasks:
- [ ] Full security scan
- [ ] Update emergency contact info
- [ ] Review user permissions
- [ ] Audit installed plugins/themes
- [ ] Test backup restoration

### Update Process Protocol
1. **Staging Environment Testing**
   - Test all updates on staging first
   - Verify functionality after each update
   - Check for conflicts

2. **Production Updates**
   - Schedule during low-traffic hours
   - Create full backup before updates
   - Update one component at a time
   - Test functionality after each update

3. **Emergency Rollback Plan**
   - Keep database backup
   - Keep file backup
   - Document rollback procedures
   - Have hosting support contacts ready

### Update Prioritization
1. **Critical Security Updates** - Apply immediately
2. **WordPress Core Updates** - Apply within 48 hours
3. **Active Plugin Updates** - Apply within 1 week
4. **Theme Updates** - Apply within 2 weeks
5. **Inactive Plugin Updates** - Remove or update monthly

## Security Monitoring & Maintenance

### Key Metrics to Monitor
- Failed login attempts per day
- Malware scan results
- Traffic anomalies
- Error log entries
- Disk space usage

### Regular Security Tasks
- Review Wordfence Central dashboard
- Check for unauthorized admin users
- Verify file integrity
- Monitor database for suspicious queries
- Review comment spam patterns

### Emergency Response Plan
1. **Suspected Compromise**
   - Take site offline immediately
   - Change all passwords
   - Run full malware scan
   - Review recent file changes

2. **Recovery Steps**
   - Clean infected files
   - Update all software
   - Strengthen security measures
   - Monitor for reinfection

---

*Last Updated: [Current Date]*
*Review and update this guide quarterly*
