// console.log('Test');
const videoAnuncio = document.getElementById('video-anuncio');

// Escuchar el avance del video
videoAnuncio.addEventListener('timeupdate', () => {
  const tiempoActual = videoAnuncio.currentTime;
  const duracion = videoAnuncio.duration;
  const porcentajeAvance = (tiempoActual / duracion) * 100;

  // Lanzar eventos en cada cuartil
  if (porcentajeAvance >= 0 && porcentajeAvance < 25) {
    window.dataLayer = window.dataLayer || [];  // Inicializar dataLayer si no existe
    window.dataLayer.push({
      'event': 'Cuartil_1',
      'porcentaje': 25,
      'avance_video': tiempoActual
    });
    console.log('Evento dataLayer Cuartil 1: ', window.dataLayer);

    // Píxel Cuartil 1
    const pixelCuartil1 = `
      <IMG SRC="https://ad.doubleclick.net/ddm/trackimp/N7872.4315966DV360MX/B30394859.411141743;dc_trk_aid=603281092;dc_trk_cid=227504314;ord=[timestamp];dc_lat=;dc_rdid=;tag_for_child_directed_treatment=;tfua=;gdpr=${GDPR};gdpr_consent=${GDPR_CONSENT_755};ltd=;dc_tdv=1?" attributionsrc BORDER="0" HEIGHT="1" WIDTH="1" ALT="Advertisement">
    `;
    document.body.insertAdjacentHTML('beforeend', pixelCuartil1);
  } else if (porcentajeAvance >= 25 && porcentajeAvance < 50) {
    window.dataLayer = window.dataLayer || [];
    window.dataLayer.push({
      'event': 'Cuartil_2',
      'porcentaje': 50,
      'avance_video': tiempoActual
    });
    console.log('Evento dataLayer Cuartil 2: ', window.dataLayer);

    // Píxel Cuartil 2
    const pixelCuartil2 = `
      <IMG SRC="https://ad.doubleclick.net/ddm/trackimp/N7872.4315966DV360MX/B30394859.411453657;dc_trk_aid=603281095;dc_trk_cid=227504317;ord=[timestamp];dc_lat=;dc_rdid=;tag_for_child_directed_treatment=;tfua=;gdpr=${GDPR};gdpr_consent=${GDPR_CONSENT_755};ltd=;dc_tdv=1?" attributionsrc BORDER="0" HEIGHT="1" WIDTH="1" ALT="Advertisement">
    `;
    document.body.insertAdjacentHTML('beforeend', pixelCuartil2);
  } else if (porcentajeAvance >= 50 && porcentajeAvance < 100) {
    window.dataLayer = window.dataLayer || [];
    window.dataLayer.push({
      'event': 'Cuartil_3',
      'porcentaje': 75,
      'avance_video': tiempoActual
    });
    console.log('Evento dataLayer Cuartil 3: ', window.dataLayer);

    // Píxel Cuartil 3
    const pixelCuartil3 = `
      <IMG SRC="https://ad.doubleclick.net/ddm/trackimp/N7872.4315966DV360MX/B30394859.411141746;dc_trk_aid=603320253;dc_trk_cid=227553083;ord=[timestamp];dc_lat=;dc_rdid=;tag_for_child_directed_treatment=;tfua=;gdpr=${GDPR};gdpr_consent=${GDPR_CONSENT_755};ltd=;dc_tdv=1?" attributionsrc BORDER="0" HEIGHT="1" WIDTH="1" ALT="Advertisement">
    `;
    document.body.insertAdjacentHTML('beforeend', pixelCuartil3);
  } else {
    window.dataLayer = window.dataLayer || [];  //
    window.dataLayer.push({
      'event': 'Cuartil_4',
      'porcentaje': 100,
      'avance_video': tiempoActual
    });
    console.log('Evento dataLayer Cuartil 4: ', window.dataLayer);

    // Píxel Cuartil 4
    const pixelCuartil4 = `
      <IMG SRC="https://ad.doubleclick.net/ddm/trackimp/N7872.4315966DV360MX/B30394859.411141749;dc_trk_aid=603320061;dc_trk_cid=227504320;ord=[timestamp];dc_lat=;dc_rdid=;tag_for_child_directed_treatment=;tfua=;gdpr=${GDPR};gdpr_consent=${GDPR_CONSENT_755};ltd=;dc_tdv=1?" attributionsrc BORDER="0" HEIGHT="1" WIDTH="1" ALT="Advertisement">
    `;
    document.body.insertAdjacentHTML('beforeend', pixelCuartil4);
  }
});
