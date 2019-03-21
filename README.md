# libvirt-php
## About this forked repository
Seems like the official libvirt-php isn't being maintenanced by anyone, contributions sent to libvirt-list was ignored, so this repository appeared.

## Additional functions
```php
resource libvirt_domain_snapshot_create_xml(resource $domain, string $xml, int $flags = 0)
bool libvirt_domain_undefine_flags(resource $domain, int $flags = 0)
bool libvirt_domain_reset(resource $domain, int $flags = 0)

int libvirt_get_last_error_code()
int libvirt_get_last_error_domain()

array libvirt_network_get_dhcp_leases(string $mac = null, int $flags = 0)
```
### Additional constants
```
enum virDomainUndefineFlagsValues {
    VIR_DOMAIN_UNDEFINE_MANAGED_SAVE	=	1 (0x1; 1 << 0)	
    Also remove any managed save
    
    VIR_DOMAIN_UNDEFINE_SNAPSHOTS_METADATA	=	2 (0x2; 1 << 1)	
    If last use of domain, then also remove any snapshot metadata
    
    VIR_DOMAIN_UNDEFINE_NVRAM	=	4 (0x4; 1 << 2)	
    Also remove any nvram file
    
    VIR_DOMAIN_UNDEFINE_KEEP_NVRAM	=	8 (0x8; 1 << 3)	
    Keep nvram file Future undefine control flags should come here.
}
```

## Origin README content

Bugfix libvirt-php required for KnightSwarm/Squire

Fixes:


1. Fix libvirt_domain_update_device not being properly defined. [8bb78b3cfb](https://github.com/KnightSwarm/libvirt-php/commit/8bb78b3cfb4d8f872f06001712202c9d63d4dd4a)

2. Fix libvirt_storagepool_get_xml_desc requiring OPTIONAL second parameter for xPath. [f89fb516ad](https://github.com/KnightSwarm/libvirt-php/commit/f89fb516ad7d75d113e26381f1bc8d48f5811158)
