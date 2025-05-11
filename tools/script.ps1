Add-Type -AssemblyName System.Device

$GeoWatcher = New-Object System.Device.Location.GeoCoordinateWatcher
$GeoWatcher.Start()

while (($GeoWatcher.Status -ne 'Ready') -and ($GeoWatcher.Permission -ne 'Denied')) {
    Start-Sleep -Milliseconds 100
}

if ($GeoWatcher.Position.Location.IsUnknown) {
    Write-Host "Konum bilgisi alınamadı."
} else {
    $latitude = $GeoWatcher.Position.Location.Latitude
    $longitude = $GeoWatcher.Position.Location.Longitude
    Write-Output "$latitude,$longitude"
}
