<script>
  export let href;
</script>

<a href={import.meta.env.VITE_CLIENT_BASE_URL + href}><slot /></a>
