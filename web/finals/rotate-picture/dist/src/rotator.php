<div class="header">
    <h1>Image Rotator</h1>
    <p>Easily rotate your images without losing quality.</p>
</div>

<?php
require_once 'vendor/autoload.php';

use lsolesen\pel\PelJpeg;
use lsolesen\pel\PelTag;
use lsolesen\pel\PelIfd;
if ($_SERVER['REQUEST_METHOD'] === 'POST') {
    $image = $_FILES['image'];
    $rotation = $_POST['rotation'];

    if ($image['error'] === UPLOAD_ERR_OK) {
        $tmpName = $image['tmp_name'];
        $name = $image['name'];
        $ext = pathinfo($name, PATHINFO_EXTENSION);
        $newName = uniqid() . '.' . $ext;
        $destination = 'uploads/' . $newName;

        if (move_uploaded_file($tmpName, $destination)) {
            $imageInfo = getimagesize($destination);
            if ($imageInfo[2] === IMAGETYPE_JPEG) {
                $jpeg = new PelJpeg($destination);
                $exif = $jpeg->getExif();
            }

            $image = imagecreatefromstring(file_get_contents($destination));
            $rotated = imagerotate($image, $rotation, 0);
            imagejpeg($rotated, $destination);
            imagedestroy($image);
            imagedestroy($rotated);

            if (isset($exif)) {
                $newJpeg = new PelJpeg($destination);
                $newJpeg->setExif($exif);
                file_put_contents($destination, $newJpeg->getBytes());
            }

            echo '<div class="content"><img src="' . $destination . '" alt="Rotated Image"></div>';
        } else {
            echo '<div class="content"><p>Failed to upload image.</p></div>';
        }
    } else {
        echo '<div class="content"><p>Failed to upload image.</p></div>';
    }
}
?>

<div class="content">
    <form action="index.php?page=rotator.php" method="post" enctype="multipart/form-data">
        <input type="file" name="image" accept="image/*" required>
        <select name="rotation" required>
            <option value="90">Rotate 90°</option>
            <option value="180">Rotate 180°</option>
            <option value="270">Rotate 270°</option>
        </select>
        <button type="submit">Rotate Image</button>
    </form>
</div>

