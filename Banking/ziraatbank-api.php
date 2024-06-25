<?php
// Ziraat Bankası API Bağlantı Ayarları
$apiUrl = "https://api.ziraatbank.com/v1/payments";
$apiKey = "YOUR_API_KEY";
$apiSecret = "YOUR_API_SECRET";

// Ödeme Bilgileri
$paymentData = array(
    "amount" => 100.00,
    "currency" => "TRY",
    "description" => "Sosyal Medya Satış",
    "customer" => array(
        "name" => "John Doe",
        "email" => "john.doe@example.com",
        "phone" => "0544909xx"
    )
);

// API İsteği
$ch = curl_init($apiUrl);
curl_setopt($ch, CURLOPT_RETURNTRANSFER, true);
curl_setopt($ch, CURLOPT_HTTPHEADER, array(
    'Content-Type: application/json',
    'X-API-Key: ' . $apiKey,
    'X-API-Secret: ' . $apiSecret
));
curl_setopt($ch, CURLOPT_POST, true);
curl_setopt($ch, CURLOPT_POSTFIELDS, json_encode($paymentData));

$response = curl_exec($ch);
$httpStatus = curl_getinfo($ch, CURLINFO_HTTP_CODE);
curl_close($ch);

// Yanıt İşleme
if ($httpStatus == 200) {
    $paymentResponse = json_decode($response, true);
    echo "Ödeme Başarılı! Ödeme Kimliği: " . $paymentResponse['id'];
} else {
    echo "Ödeme İşlemi Başarısız. Hata Kodu: " . $httpStatus;
}
?>
