<?php
class Api {
    // API URL
    public $api_url = 'https://follow.sale/api/v1'; 

    // Your API key
    public $api_key = 'bpmFYCXTVFGa8vaSqK33bcg0bxrCmFDJ'; 

    /**
     *
     * Add Order
     *
     */
    public function add_order($data) { 
        $post = array_merge(array('key' => $this->api_key, 'action' => 'add'), $data);
        $result = $this->connect($post);
        return json_decode($result);
    }

    /**
     *
     * Order status
     *
     */
    public function status($order_id) { 
        $result = $this->connect(array(
            'key'    => $this->api_key,
            'action' => 'status',
            'order'  => $order_id
        ));
        return json_decode($result);
    }

    /**
     *
     * Order multi status
     *
     */

    public function multi_status($order_ids) { 
        $result = $this->connect(array(
            'key'        => $this->api_key,
            'action'     => 'status',
            'orders'     => implode(",", (array)$order_ids)
        ));
        return json_decode($result);
    }


    /**
     *
     * All services
     *
     */
    public function services() { 
        $result = $this->connect(array(
            'key'     => $this->api_key,
            'action'  => 'services',
        ));
        return json_decode($result);
    }

    /**
     *
     * Balance
     *
     */
    public function balance() { 
        $result = $this->connect(array(
            'key'     => $this->api_key,
            'action'  => 'balance',
        ));
        return json_decode($result);
    }

    /**
     *
     * Connect to panel
     *
     */
    private function connect($post) {
        $_post = Array();

        if (is_array($post)) {
          foreach ($post as $name => $value) {
            $_post[] = $name.'='.urlencode($value);
          }
        }

        if (is_array($post)) {
          $url_complete = join('&', $_post);
        }
        $url = $this->api_url."?".$url_complete;

        $ch = curl_init($url);
        curl_setopt($ch, CURLOPT_RETURNTRANSFER, 1);
        curl_setopt($ch, CURLOPT_HEADER, 0);
        curl_setopt($ch, CURLOPT_FOLLOWLOCATION, true);
        curl_setopt($ch, CURLOPT_USERAGENT, 'API (compatible; MSIE 5.01; Windows NT 5.0)');
        $result = curl_exec($ch);
        if (curl_errno($ch) != 0 && empty($result)) {
          $result = false;
        }
        curl_close($ch);
        return $result;
    }

}

// Examples
$api = new Api();

# return all services
$services = $api->services(); 

# return user balance
$balance = $api->balance(); 

// add order
$order = $api->order(array('service' => 1, 'link' => 'http://example.com/test', 'quantity' => 100)); # Default

$order = $api->order(array('service' => 1, 'link' => 'http://example.com/test', 'comments' => "good pic\ngreat photo\n:)\n;)")); # Custom Comments

$order = $api->order(array('service' => 1, 'link' => 'http://example.com/test', 'quantity' => 100, 'runs' => 10, 'interval' => 60)); # Drip-feed

# return status, charge, remains, start count, order_id
$status = $api->status(23); 

# return orders status, charge, remains, start count, order_id
$statuses = $api->multi_status([12, 2, 13]); 
